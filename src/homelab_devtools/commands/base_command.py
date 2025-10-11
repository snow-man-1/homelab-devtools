# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from collections.abc import Callable
from typing import Any

from typer import Exit as Typer_Exit
from typer import Typer

from src.homelab_devtools.errors import BusinessLogicError, InputError


class BaseCommand:
    def __init__(
        self,
        command_group: str,
        app: Typer | None = None,
    ) -> None:
        self.command_group: str = command_group
        self.app: Typer = app or Typer()

    def wrap_error_handling(self, func: Callable) -> Callable:
        def error_handling_wrapper(*args: Any, **kwargs: Any) -> None:
            try:
                func(*args, **kwargs)
            except InputError as input_error:
                # everything related to user inputs
                raise Typer_Exit(code=1) from input_error
            except BusinessLogicError as business_logic_error:
                # everything related to business logic errors
                raise Typer_Exit(code=2) from business_logic_error
            except SystemError as system_error:
                # everything which isn't business logic and input inside
                # the application like access to files
                raise Typer_Exit(code=3) from system_error
            # everything between 3 and 100 is reserved for more
            # specific application related error types
            except Exception as error:
                # everything which is unexpected
                raise Typer_Exit(code=100) from error

        return error_handling_wrapper
