# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typer import Typer


class BaseCommand:
    def __init__(
        self,
        command_group: str,
        app: Typer | None = None,
    ) -> None:
        self.command_group: str = command_group
        self.app: Typer = app or Typer()
