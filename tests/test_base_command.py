# SPDX-License-Identifier: MIT
"""
Test class for Unit Testing the BaseCommand class which describes the base for any typer commands
Author: snow-man-1
"""

from src.homelab_devtools.commands.base_command import BaseCommand


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
