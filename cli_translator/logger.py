#!/usr/bin/env python3
"""general logging stuff"""

# pylint: disable=logging-fstring-interpolation

import logging

from sys import stderr


def configure_root_logger(debug: bool):
    """
    configure the global/module level root logger

    - output all logging messages to STDERR only
    - more detailed format for DEBUG, less detailed format else
    """

    message_format: str
    date_format: str | None
    level: int

    if debug:
        message_format = (
            "%(asctime)s [%(levelname)s] %(module)s - %(name)s"
            "  - %(funcName)s - %(lineno)s: %(message)s"
        )
        date_format = None  # aka 'use the very detailed default'
        level = logging.DEBUG

    else:
        message_format = "%(asctime)s [%(levelname)s] %(message)s"
        date_format = "%Y-%m-%dT%H:%M:%S"
        level = logging.WARNING

    logging.basicConfig(
        format=message_format,
        datefmt=date_format,
        level=level,
        stream=stderr,
    )


def log_args_and_return_value(func):
    """a decorator to log args and return values"""

    def wrap(*args, **kwargs):
        # log the function name and arguments
        logging.debug(
            f"calling {func.__name__} with args: {args}, kwargs: {kwargs}", stacklevel=2
        )

        # call the original function
        result = func(*args, **kwargs)

        # log the return value
        logging.debug(f"{func.__name__} returned: {result}", stacklevel=2)

        # return the result
        return result

    return wrap
