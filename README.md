# CLI Translator

~~~
Turn your current cli into a translator.

- The key functionalty comes with: https://pypi.org/project/deepl/
- You'll need a DeepL Authentication Key. It will be stored in your systems keyring.
- It just needs to be set once, using the -auth [Your-Key] argument.
- You can delete it from your keyring again, using the -del_auth argument.

You'll need to pass source and target language. You can use the arguments for it,
but you'll be prompted for it if you don't.

When you're prompted for it, you can get a list of the supported codes.

options:
  -h, --help            show this help message and exit
  -auth, --authentication_key AUTHENTICATION_KEY
                        set or update your authentication key to the given value
  -slc, --source_language_code SOURCE_LANGUAGE_CODE
                        set the language code for source language
  -tlc, --target_language_code TARGET_LANGUAGE_CODE
                        set the language code for target language
  -del_auth, --delete_authentication_key
                        delete the authentication key from your local keyring
  -d, --debug           turn on debug mode, outputs to STDERR
  -v, --version         show program's version number and exit

Have fun!
~~~

## Example execution

~~~
cli_translator.py
Please provide a source language code [type 'list' to list supported source languages]: EN
Please provide a target language code [type 'list' to list supported target languages]: FR

Translating English to French
Press [CTRL+C] to terminate

[translate EN => FR]: Hello World!


Bonjour le monde !
~~~

## Requirements

- Created with Python 3.11.4
- Highest Version testet so far: Python 3.13 (September 2025)
- [DeepL authentication key](https://www.deepl.com) (As of September 2023 it is free, but you still need a credit card)
- Some default Keyring implementation to store your authentication key with [keyring](https://pypi.org/project/keyring/)

## Setup & Run

### Setup your Python environment

I'd always go for a virtual Python environment, to be independant of the oss installation,
but it is not a hard requirment of course.

* In example with pyenv you can install a desired Python version.
* In example with venv you can use this Python version to create your virtual environment.

~~~
# use pyenv to install the desired Python version
pyenv install 3.11.4

# use this version to create your venv in your desired location
/home/${USER}/.pyenv/versions/3.11.4/bin/python3.11 -m venv cli_translator

# henceforth active it before using the cli-translator
source cli_translator/bin/activate
~~~

### Install requirements

~~~
# use your desired python env, go to the applications root directory
# and install the required pypi packages via pip
python3 -m pip install -r requirements.txt
~~~

### Run the application

Let the main script/application explain the rest. You need to pass your
authentication key only once and the desired languages for each execution.

~~~
cli_translator.py -h
~~~

## Sources:

- [Structuring a Python Projet](https://realpython.com/python-application-layouts/)
- [Open Source Initiative: Zero-Clause BSD](https://opensource.org/license/0bsd/)
- [DeepL Python Library](https://pypi.org/project/deepl/)
- [Keyring Python Library](https://pypi.org/project/keyring/)
