# SPDX-License-Identifier: MIT
"""
This module contains a factory which contains all command classes which needs to be added in the main typer instance
Author: snow-man-1
"""

from collections.abc import Callable

from typer import Typer

from homelab_devtools.commands.base_command import BaseCommand
from homelab_devtools.commands.main_command import MainCommand
from homelab_devtools.errors import TyperSetupError


class CliFactory:
    def create_cli_app(self) -> Typer:
        """Factory method to create a Typer Cli app

        Returns:
            Typer: the main Typer instance conainting all sub commands out of the command objects
        """
        main_cli_app = Typer()
        command_registered_callback: BaseCommand | None = None
        command_list = self.setup_commands()
        for command in command_list:
            built_commands = self.build_commands(command)
            built_callback = self.build_callback(command, command_registered_callback)
            if built_callback:
                command_registered_callback = command

            prepared_typer = self.prepare_typer_with_items(
                built_commands, built_callback, command.app
            )

            command.app = prepared_typer
            main_cli_app.add_typer(prepared_typer)
        return main_cli_app

    def build_commands(self, command: BaseCommand) -> dict[str, Callable]:
        cli_commands = self.get_cli_commands_of_command(command)
        prepared_cli_commands = self.wrap_cli_commands_with_error_handling(
            command, cli_commands
        )
        return prepared_cli_commands

    def build_callback(
        self,
        command: BaseCommand,
        command_registered_callback: BaseCommand | None,
    ) -> Callable | None:
        """Prepare function in command marked with as_typer_callback
        for adding it to typer

        Args:
            command (BaseCommand): command which contains functions with as_typer_callback
            already_registered (BaseCommand | None): command which added a callback

        Raises:
            TyperSetupError: More than 1 methods are marked with as_typer_callback

        Returns:
            Callable: Method ready to be added to typer
        """
        cli_callbacks = self.get_cli_callbacks_of_command(command)

        # no method marked as typer callback
        if len(cli_callbacks) == 0:
            return None

        # only 1 callback is allowed
        if len(cli_callbacks) > 1:
            raise TyperSetupError("The use of as_typer_callback is limited to 1")

        if isinstance(command_registered_callback, BaseCommand):
            # there is already a typer callback from another command
            raise TyperSetupError(
                f"The command {command_registered_callback.__class__.__name__} already registered 1 callback"
            )

        # get only element in dict
        key = next((key for key in cli_callbacks.keys()), "")
        return cli_callbacks.get(key)

    def setup_commands(self) -> list[BaseCommand]:
        """Instantiates all Command Objects which will be available in the cli and list all of the Typer instances

        Returns:
            list[Typer]: All Typer instances contained in the command classes
        """
        commands: list[BaseCommand] = []

        # default command for commands like version and basic options
        main_command: MainCommand = MainCommand()

        # add available commands to list
        commands.append(main_command)

        return commands

    def get_cli_commands_of_command(self, command: BaseCommand) -> dict[str, Callable]:
        if not command:
            return {}

        result = {}

        for name, attribute in command.__class__.__dict__.items():
            if callable(attribute) and getattr(attribute, "is_typer_command", False):
                result[name] = attribute

        return result

    def get_cli_callbacks_of_command(self, command: BaseCommand) -> dict[str, Callable]:
        if not command:
            return {}

        result = {}

        for name, attribute in command.__class__.__dict__.items():
            if callable(attribute) and getattr(attribute, "is_typer_allback", False):
                result[name] = attribute

        return result

    def wrap_cli_commands_with_error_handling(
        self, command: BaseCommand, command_list: dict[str, Callable]
    ) -> dict[str, Callable]:
        if not command_list:
            return {}

        if not command:
            return command_list

        return {
            key: command.wrap_error_handling(func) for key, func in command_list.items()
        }

    def prepare_typer_with_items(
        self,
        commands: dict[str, Callable],
        callback: Callable | None,
        app: Typer,
    ) -> Typer:
        if commands:
            app = self.prepare_typer_with_cli_commands(commands, app)

        if callback:
            app = self.prepare_typer_with_cli_callback(callback, app)

        return app

    def prepare_typer_with_cli_commands(
        self,
        command_list: dict[str, Callable],
        app: Typer,
    ) -> Typer:
        if not command_list or not app:
            return app

        for command, method in command_list.items():
            app.command(name=command)(method)

        return app

    def prepare_typer_with_cli_callback(
        self,
        callback: Callable | None,
        app: Typer,
    ) -> Typer:
        if not app:
            return app

        if not callback or not callable(callback):
            return app

        # typer supports only 1 callback
        app.callback()(callback)

        return app
