# SPDX-License-Identifier: MIT
"""
Test class for Unit Testing the BaseCommand class which describes the base for any typer commands
Author: snow-man-1
"""

from pytest import raises
from pytest_mock import MockerFixture

from src.homelab_devtools.commands.base_command import BaseCommand
from tests.conftest import MockCommand


class TestBaseCommand:
    """
    The BaseCommand is the base for all command classes which offers typer commands.
    It should:
    1. bring a typer instance which can be added in the registry when creating a cli app, so that all extending classes has it.
    2. it contains a name attribute defining the command group
    """

    def test_instance_has_name_and_typer_instance(self, mock_typer):
        command_group = "test"
        command = BaseCommand(command_group, app=mock_typer)
        assert hasattr(command.app, "command")
        assert command.command_group == command_group

    def test_input_error_handling(
        self,
        mocker: MockerFixture,
        mock_command: MockCommand,
    ):
        wrapped_typer_command = mock_command.wrap_error_handling(
            mock_command.test_with_user_input_error
        )

        mock_typer_exit = mocker.patch(
            "src.homelab_devtools.commands.base_command.Typer_Exit",
            side_effect=SystemExit,
        )

        with raises(SystemExit):
            wrapped_typer_command()

        mock_typer_exit.assert_called_once_with(code=1)

    def test_business_logic_error_handling(
        self,
        mocker: MockerFixture,
        mock_command: MockCommand,
    ):
        wrapped_typer_command = mock_command.wrap_error_handling(
            mock_command.test_with_business_logic_error
        )

        mock_typer_exit = mocker.patch(
            "src.homelab_devtools.commands.base_command.Typer_Exit",
            side_effect=SystemExit,
        )

        with raises(SystemExit):
            wrapped_typer_command()

        mock_typer_exit.assert_called_once_with(code=2)

    def test_system_error_handling(
        self,
        mocker: MockerFixture,
        mock_command: MockCommand,
    ):
        wrapped_typer_command = mock_command.wrap_error_handling(
            mock_command.test_with_system_error
        )

        mock_typer_exit = mocker.patch(
            "src.homelab_devtools.commands.base_command.Typer_Exit",
            side_effect=SystemExit,
        )

        with raises(SystemExit):
            wrapped_typer_command()

        mock_typer_exit.assert_called_once_with(code=3)

    def test_unexpected_error_handling(
        self,
        mocker: MockerFixture,
        mock_command: MockCommand,
    ):
        wrapped_typer_command = mock_command.wrap_error_handling(
            mock_command.test_with_unexpected_error
        )

        mock_typer_exit = mocker.patch(
            "src.homelab_devtools.commands.base_command.Typer_Exit",
            side_effect=SystemExit,
        )

        with raises(SystemExit):
            wrapped_typer_command()

        mock_typer_exit.assert_called_once_with(code=100)
