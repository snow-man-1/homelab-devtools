# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""
from typing import Any

from typer import Typer


class CommandRegistry:
    def __init__(self) -> None:
        self.typer_commands: dict[str, Any] = {}

    def create_cli_app(self) -> Typer:
        return Typer()

    def register(self, command_group: str, command: Typer) -> None:
        self.typer_commands[command_group] = command

    def get_command(self, command_group: str) -> Typer | None:
        return self.typer_commands.get(command_group)
