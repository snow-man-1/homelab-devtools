# SPDX-License-Identifier: MIT
"""
This module contains a factory which contains all command classes which needs to be added in the main typer instance
Author: snow-man-1
"""

from collections.abc import Callable

from typer import Typer

from homelab_devtools.commands.base_command import BaseCommand


class CliFactory:
    def create_cli_app(self) -> Typer:
        """Factory method to create a Typer Cli app

        Returns:
            Typer: the main Typer instance conainting all sub commands out of the command objects
        """
        main_cli_app = Typer()
        command_list = self.setup_commands()
        for command in command_list:
            cli_commands = self.get_cli_commands_of_command(command)
            prepared_typer = self.prepare_typer_with_cli_commands(
                cli_commands, command.app
            )
            command.app = prepared_typer
            main_cli_app.add_typer(prepared_typer)
        return main_cli_app

    def setup_commands(self) -> list[BaseCommand]:
        """Instantiates all Command Objects which will be available in the cli and list all of the Typer instances

        Returns:
            list[Typer]: All Typer instances contained in the command classes
        """
        commands: list[BaseCommand] = []

        # TODO instantiate all commands which are available in cli

        return commands

    def get_cli_commands_of_command(self, command: BaseCommand) -> dict[str, Callable]:
        if not command:
            return {}

        result = {}

        for name, attribute in command.__class__.__dict__.items():
            if callable(attribute) and getattr(attribute, "is_typer_command", False):
                result[name] = attribute

        return result

    def prepare_typer_with_cli_commands(
        self, command_list: dict[str, Callable], app: Typer
    ) -> Typer:
        if not command_list or not app:
            return app

        for command, method in command_list.items():
            app.command(name=command)(method)

        return app
