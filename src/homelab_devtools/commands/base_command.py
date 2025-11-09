# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from collections.abc import Callable
from typing import Any

import typer

from homelab_devtools.errors import (
    ApplicationError,
    InputError,
)


class BaseCommand:
    def __init__(
        self,
        command_group: str = "",
        app: typer.Typer | None = None,
    ) -> None:
        self.command_group: str = command_group
        self.app: typer.Typer = app or typer.Typer()

    def wrap_error_handling(self, func: Callable) -> Callable:
        def error_handling_wrapper(*args: Any, **kwargs: Any) -> None:
            try:
                func(*args, **kwargs)
            except (ApplicationError, InputError) as app_error:
                print(f"id of exception in applicationerror {id(app_error)}")
                raise typer.Exit(code=app_error.typer_exit_code) from app_error
            except Exception as e:
                print(f"id of exception in exception case {id(e)}")
                # everything which is unexpected
                unexpected_error = ApplicationError(f"Unexpected error occured: {e}")
                raise typer.Exit(code=unexpected_error.typer_exit_code) from e

        return error_handling_wrapper
