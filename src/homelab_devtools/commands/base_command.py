# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typer import Typer


class BaseCommand:
    def __init__(self, command_group: str) -> None:
        self.app: Typer = Typer()
        self.command_group: str = command_group
