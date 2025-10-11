# SPDX-License-Identifier: MIT
"""
This module contains different Error Classes describing different types of wrong states like user input errors and business logic errors
Author: snow-man-1
"""


class ApplicationError(Exception):
    """Base Class for application related errors like input, business logic or system errors"""

    pass


class BusinessLogicError(Exception):
    """Class for business logic errors"""

    pass


class InputError(ApplicationError):
    """Class for User Input Errors"""

    pass


class ExternalError(ApplicationError):
    """Class for everything which is not of the app itself like business logic or input like access to a file failed"""

    pass
