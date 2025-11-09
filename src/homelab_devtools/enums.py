# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

import enum


class ErrorExitCodes(enum.IntEnum):
    """Exit Codes for typer depending on the error type

    The value needs to be between 1 and 127
    """

    INPUT_ERROR = 1
    BUSINESS_LOGIC_ERROR = 2
    EXTERNAL_ERROR = 3
    TYPER_SETUP_ERROR = 4
    APPLICATION_ERROR = 100
