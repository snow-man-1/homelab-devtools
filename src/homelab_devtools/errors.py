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


class SystemError(ApplicationError):
    """Class for everything which is not input or business logic error inside the application context like access to a file failed"""

    pass
