# SPDX-License-Identifier: MIT
"""
This module contains a factory which contains all command classes which needs to be added in the main typer instance
Author: snow-man-1
"""

from typing import Any

from typer import Typer


class CliFactory:
    def __init__(self) -> None:
        self.typer_commands: dict[str, Any] = {}

    def create_cli_app(self) -> Typer:
        """Factory method to create a Typer Cli app

        Returns:
            Typer: the main Typer instance conainting all sub commands out of the command objects
        """
        return Typer()

    def setup_commands(self) -> list[Typer]:
        """Instantiates all Command Objects which will be available in the cli and list all of the Typer instances

        Returns:
            list[Typer]: All Typer instances contained in the command classes
        """
        commands: list[Typer] = []
        return commands
