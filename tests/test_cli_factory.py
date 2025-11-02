# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from collections.abc import Callable
from typing import Any

from pytest_mock import MockerFixture

from homelab_devtools.cli_factory import CliFactory
from homelab_devtools.commands.base_command import BaseCommand
from tests.conftest import MockCommand, MockTyper


class TestCliFactory:
    """
    The typer factory should have the following behaviour:
    1. it instantiates all commands available in the cli via a method
    2. it can create a complete typer object for the main module to execute
    """

    def test_factory_can_create_cli_app(
        self,
        cli_factory: CliFactory,
        mocker: MockerFixture,
        mock_typer: MockTyper,
        mock_command: MockCommand,
    ):
        mocker.patch("homelab_devtools.cli_factory.Typer", return_value=mock_typer)
        mocker.patch.object(cli_factory, "setup_commands", return_value=[mock_command])
        mocker.patch.object(
            cli_factory,
            "get_cli_commands_of_command",
            return_value={"test": lambda x: None},
        )
        mocker.patch.object(
            cli_factory,
            "wrap_cli_commands_with_error_handling",
            return_value={"test": lambda x: None},
        )
        mocker.patch.object(
            cli_factory,
            "prepare_typer_with_cli_commands",
            return_value=mock_typer,
        )

        cli_instance: Any = cli_factory.create_cli_app()
        assert cli_instance is mock_typer

    def test_factory_can_get_a_list_of_command_objects(self, cli_factory: CliFactory):
        commands: list[BaseCommand] = cli_factory.setup_commands()
        assert all(isinstance(command, BaseCommand) for command in commands)

    def test_get_all_cli_commands_of_command(
        self, mock_command: BaseCommand, cli_factory: CliFactory
    ):
        cli_commands: dict[str, Callable] = cli_factory.get_cli_commands_of_command(
            mock_command
        )
        assert len(cli_commands.keys()) == 1

    def test_wrap_cli_commands_with_error_handling(
        self,
        mock_command: BaseCommand,
        cli_factory: CliFactory,
    ):
        command_list = {"test": lambda x: None}
        cli_commands: dict[str, Callable] = (
            cli_factory.wrap_cli_commands_with_error_handling(
                mock_command,
                command_list,
            )
        )

        assert cli_commands["test"].__name__ == "error_handling_wrapper"

    def test_prepare_typer_with_cli_commands_of_command(
        self, mock_typer: Any, cli_factory: CliFactory
    ):
        command_list = {"test": lambda x: None}
        prepared_typer = cli_factory.prepare_typer_with_cli_commands(
            command_list, mock_typer
        )
        assert any(
            command.name == "test" for command in prepared_typer.registered_commands
        )
