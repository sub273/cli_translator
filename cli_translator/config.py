#!/usr/bin/env python3
"""
Define the configuration

No classical fixed values you need to change, so: no classic config file.
"""

# standard imports
from dataclasses import dataclass

# local imports
from logger import log_args_and_return_value
from languages import Language


@dataclass
class Config:
    """store configuration properties"""

    keyring_service: str  # service name used for keyring
    keyring_username: str  # user name used for keyring
    deepl_authentication_key: str  # authentication key used for deepl
    source_language: Language  # selected source language
    target_language: Language  # selected target language


@log_args_and_return_value
def get_config() -> Config:
    """init and return configuration object"""

    # just a random uuid you will probably not have used as a name in your keyring until now
    app_id = "cli-translator-6d2d68a9-bac5-479f-8fc4-825b8661bbb7"

    return Config(
        keyring_service=app_id,
        keyring_username=app_id,
        deepl_authentication_key="",
        source_language="",
        target_language="",
    )
