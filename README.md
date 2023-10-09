# CLI Translator

Turn your current cli into a translator.

- The key functionalty comes with: https://pypi.org/project/deepl/
- You'll need a DeepL Authentication Key. It will be stored in your local systems keyring.

You'll need to pass source and target language. You can use the arguments for it,
but you'll be prompted for it if you don't.

When you're prompted for it, you can get a list of the supported codes.

## Example

~~~
Please provide a source language code [type 'list' to list supported source languages]: EN
Please provide a target language code [type 'list' to list supported target languages]: FR

Translating English to French
Press [CTRL+C] to terminate

[translate EN => FR]: Hello World!


Bonjour le monde !
~~~

## Requirements

- Created with Python 3.11.4
- [DeepL authentication key](https://www.deepl.com) (As of September 2023 it is free, but you still need a credit card)
- Some default Keyring implementation to store your authentication key with [keyring](https://pypi.org/project/keyring/)

## Setup & Run

I'd always go for a virtual Python environment, but it is not a hard requirment of course.

~~~
# create & activate a venv in your desired location
python3 -m venv cli_translator
source cli_translator/bin/activate

# go to the desired applications root directory and
# install the required pypi packages via requirements.txt
python3 -m pip install -r requirements.txts

# let the main script/application explain the rest
# (setup authentication and languages)
cli_translator.py -h
~~~

## Sources:

- [Structuring a Python Projet](https://realpython.com/python-application-layouts/)
- [Open Source Initiative: Zero-Clause BSD](https://opensource.org/license/0bsd/)
- [DeepL Python Library](https://pypi.org/project/deepl/)
- [Keyring Python Library](https://pypi.org/project/keyring/)

## Releases

- 20231009.1958: Initial Release
- 20231009.2200: Fixed CVEs
  - Updated urllib3 and cryptography versions from pypi
