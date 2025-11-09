# SPDX-License-Identifier: MIT
"""
This module contains different Error Classes describing different types of wrong states like user input errors and business logic errors
Author: snow-man-1
"""

from homelab_devtools.enums import ErrorExitCodes


class ApplicationError(Exception):
    """Base Class for application related errors like input, business logic or system errors"""

    def __init__(
        self,
        message: str,
        typer_exit_code: int = ErrorExitCodes.APPLICATION_ERROR.value,
    ):
        super().__init__(message)
        self.typer_exit_code = typer_exit_code


class InputError(ApplicationError):
    """Class for User Input Errors"""

    def __init__(
        self,
        message: str,
        typer_exit_code: int = ErrorExitCodes.INPUT_ERROR.value,
    ):
        super().__init__(message, typer_exit_code)


class BusinessLogicError(ApplicationError):
    """Class for business logic errors"""

    def __init__(
        self,
        message: str,
        typer_exit_code: int = ErrorExitCodes.BUSINESS_LOGIC_ERROR.value,
    ):
        super().__init__(message, typer_exit_code)


class ExternalError(ApplicationError):
    """Class for everything which is not of the app itself like business logic or input like access to a file failed"""

    def __init__(
        self,
        message: str,
        typer_exit_code: int = ErrorExitCodes.EXTERNAL_ERROR.value,
    ):
        super().__init__(message, typer_exit_code)


class TyperSetupError(ApplicationError):
    """Class for errors occuring while setup typer"""

    def __init__(
        self,
        message: str,
        typer_exit_code: int = ErrorExitCodes.TYPER_SETUP_ERROR.value,
    ):
        super().__init__(message, typer_exit_code)
