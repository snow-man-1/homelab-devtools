# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typer import Typer

from homelab_devtools.cli_factory import CliFactory


class TestTyperFactory:
    """
    The typer factory should have the following behaviour:
    1. it instantiates all commands available in the cli via a method
    2. it can create a complete typer object for the main module to execute
    """

    def test_factory_can_create_cli_app(self, cli_factory: CliFactory):
        cli_instance: Typer = cli_factory.create_cli_app()
        assert isinstance(cli_instance, Typer)

    def test_factory_can_get_a_list_of_typer_objects(self, cli_factory: CliFactory):
        commands: list[Typer] = cli_factory.setup_commands()
        assert all(isinstance(command, Typer) for command in commands)
