# SPDX-License-Identifier: MIT
"""
Test class for Unit Testing the BaseCommand class which describes the base for any typer commands
Author: snow-man-1
"""

from typer import Typer

from homelab_devtools.commands.base_command import BaseCommand


class TestBaseCommand:
    """
    The BaseCommand is the base for all command classes which offers typer commands.
    It should:
    1. bring a typer instance which can be added in the registry when creating a cli app, so that all extending classes has it.
    2. it has a method which collects all methods of the subclass marked with a decorator like as_typer_command to define a method as
       actual typer command
    3. it contains a name attribute defining the command group
    """

    def test_instance_has_name_and_typer_instance(self, mock_typer):
        command_group = "test"
        command = BaseCommand(command_group)
        assert isinstance(command.app, Typer)
        assert command.command_group == command_group
