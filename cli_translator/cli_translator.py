#!/usr/bin/env python3
"""Execute this to run the application, doing so:use -h for help to get some help"""

# pylint: disable=logging-fstring-interpolation, import-error, broad-except

__version__ = "20231029.2029"

# standard imports
import argparse
import logging
from dataclasses import dataclass
from os.path import basename
from sys import exit as sys_exit
from textwrap import dedent
from typing import List

# third party imports
import keyring
import deepl

# local imports
from config import Config, get_config
from languages import LanguageType, source_languages, target_languages
from logger import configure_root_logger, log_args_and_return_value


@dataclass
class Arguments:
    """Provide an ide friendly args-object"""

    debug: bool
    authentication_key: str | None
    source_language_code: str | None
    target_language_code: str | None
    delete_authentication_key: bool


def get_arguments() -> Arguments:
    """Handle arguments and set description"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=dedent(
            """\
            Turn your current cli into a translator.

            - The key functionalty comes with: https://pypi.org/project/deepl/
            - You'll need a DeepL Authentication Key. It will be stored in your systems keyring.
            - It just needs to be set once, using the -auth [Your-Key] argument.
            - You can delete it from your keyring again, using the -del_auth argument.

            You'll need to pass source and target language. You can use the arguments for it,
            but you'll be prompted for it if you don't.

            When you're prompted for it, you can get a list of the supported codes.
            """
        ),
        epilog="Have fun!",
    )
    parser.add_argument(
        "-auth",
        "--authentication_key",
        help="set or update your authentication key to the given value",
    )
    parser.add_argument(
        "-slc",
        "--source_language_code",
        help="set the language code for source language",
    )

    parser.add_argument(
        "-tlc",
        "--target_language_code",
        help="set the language code for target language",
    )

    parser.add_argument(
        "-del_auth",
        "--delete_authentication_key",
        help="delete the authentication key from your local keyring",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="turn on debug mode, outputs to STDERR",
        action="store_true",
    )

    parser.add_argument("-v", "--version", action="version", version=__version__)

    parse_args_args = parser.parse_args()

    return Arguments(
        debug=parse_args_args.debug,
        authentication_key=parse_args_args.authentication_key,
        source_language_code=parse_args_args.source_language_code,
        target_language_code=parse_args_args.target_language_code,
        delete_authentication_key=parse_args_args.delete_authentication_key,
    )


@log_args_and_return_value
def print_languages(language_type: LanguageType):
    """print source or target languages: code - name"""
    if language_type == language_type.SOURCE:
        languages = source_languages
    else:
        languages = target_languages

    for language in languages.values():
        print(f"{language.code} - {language.name}")


@log_args_and_return_value
def ask_for_language(language_type: LanguageType) -> str:
    """prompt for language"""

    user_input = read_user_input(
        f"Please provide a {language_type} language code "
        f"[type 'list' to list supported {language_type} languages]: "
    )

    logging.debug(f"{input=}")

    if not user_input:
        user_input = ask_for_language(language_type)

    if user_input == "list":
        print_languages(language_type)
        user_input = ask_for_language(language_type)

    return user_input


def setup_languages(config: Config, arguments: Arguments) -> None:
    """setup languages for this excecution"""

    source_language_code: str
    target_language_code: str

    if not arguments.source_language_code:
        source_language_code = ask_for_language(LanguageType.SOURCE)
    else:
        source_language_code = arguments.source_language_code

    if source_language_code not in source_languages:
        exit_error(
            f"'{source_language_code}' is not in the list of supported "
            f"{LanguageType.SOURCE} languages {', '.join(source_languages.keys())}."
        )
    else:
        config.source_language = source_languages[source_language_code]

    if not arguments.target_language_code:
        target_language_code = ask_for_language(LanguageType.TARGET)
    else:
        target_language_code = arguments.target_language_code

    if target_language_code not in target_languages:
        exit_error(
            f"'{target_language_code}' is not in the list of supported "
            f"{LanguageType.TARGET} languages {', '.join(target_languages.keys())}."
        )
    else:
        config.target_language = target_languages[target_language_code]


def setup_authentication(config: Config, arguments: Arguments) -> None:
    """setup authentication key with keyring"""

    # delete key if desired
    if arguments.delete_authentication_key:
        try:
            keyring.delete_password(config.keyring_service, config.keyring_username)
            print("Your authentication key has been deleted from your keyring.")
        except keyring.errors.PasswordDeleteError as exception:
            print(
                f"Your authentication key was not be deleted from your keyring: {exception}"
            )

    # add provided authentication key to keyring
    if arguments.authentication_key:
        keyring.set_password(
            config.keyring_service,
            config.keyring_username,
            arguments.authentication_key,
        )

    # retrieve key from keyring and add authentication key from keyring to config
    config.deepl_authentication_key = keyring.get_password(
        config.keyring_service, config.keyring_username
    )

    if not config.deepl_authentication_key:
        exit_info(
            "\nTo use the CLI-Translator: Please provide your deepl "
            "authentication-key by using auth-argument:\n\n"
            f"{basename(__file__)} -auth [AUTHENTICATION_KEY]\n"
        )

    logging.debug(f"{config=}")


def exit_error(message: str) -> None:
    """exit 'not ok' with custom text"""
    print(f"{message}")
    sys_exit(1)


def exit_info(message: str) -> None:
    """exit 'ok' with custom message"""
    print(f"{message}")
    sys_exit(0)


def translate(text_to_translate: str, config: Config) -> List[deepl.TextResult]:
    """do the deepl call and print the translation"""

    translator: deepl.Translator
    result: deepl.TextResult | [deepl.TextResult]

    try:
        translator = deepl.Translator(config.deepl_authentication_key)
    except Exception as exception:
        exit_error(f"Could not create tranlator: {exception}")

    try:
        result = translator.translate_text(
            text_to_translate,
            target_lang=config.target_language.code,
            source_lang=config.source_language.code,
        )
    except deepl.exceptions.AuthorizationException:
        exit_error("Authorization failure, best to check your authentication key.")
    except Exception as exception:
        exit_error(f"Could not translate text: {exception}")

    # unify to a list, if we didn't get one allready
    if not isinstance(result, list):
        result = [result]

    return result


def print_to_stdout(translated_text: List[deepl.TextResult]) -> None:
    """output the translation to standard out"""
    print("\n")
    for text_result in translated_text:
        print(text_result)
    print("\n")


def ask_for_input_forever(config: Config) -> None:
    """loop for input to translate"""
    while True:
        text_to_translate = read_user_input(
            f"[translate {config.source_language.code} => {config.target_language.code}]: "
        )
        translated_text = translate(text_to_translate, config)
        print_to_stdout(translated_text)


def read_user_input(prompt: str) -> str:
    """read and return user input"""

    user_input: str

    user_input = ""

    try:
        while user_input == "":
            user_input = input(prompt)
    except (KeyboardInterrupt, EOFError):
        exit_info(message="\nTerminated by User")

    return user_input


def print_greeting(config: Config) -> None:
    """print languages to translate and the exit instruction"""
    print(
        f"\nTranslating {config.source_language.name} to {config.target_language.name} \n"
        "Press [CTRL+C] to terminate\n"
    )


def main(arguments: Arguments) -> None:
    """do it all"""

    config = get_config()
    setup_authentication(config, arguments)
    setup_languages(config, arguments)

    logging.debug(config)
    print_greeting(config)
    ask_for_input_forever(config)


if __name__ == "__main__":
    args = get_arguments()
    configure_root_logger(args.debug)
    logging.debug(f"{args=}")

    main(args)
    sys_exit(0)
