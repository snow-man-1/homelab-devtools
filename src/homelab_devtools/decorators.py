# SPDX-License-Identifier: MIT
"""
This module contains a list of decorators used in this project

Author: snow-man-1
"""

from collections.abc import Callable


def as_typer_command(func: Callable) -> Callable:
    func.is_typer_command = True  # type: ignore
    return func


def as_typer_callback(func: Callable) -> Callable:
    func.is_typer_callback = True  # type: ignore
    return func
