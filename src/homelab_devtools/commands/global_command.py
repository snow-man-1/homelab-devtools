# SPDX-License-Identifier: MIT
"""
This module contains a class which contains all the global commands for the base typer instance
Author: snow-man-1
"""

import typer

from homelab_devtools.commands.base_command import BaseCommand


class GlobalCommand(BaseCommand):
    def __init__(self, command_group: str = "", app: typer.Typer = None) -> None:
        app = typer.Typer(invoke_without_command=True)
        super().__init__(command_group, app)

    def prepare_base_typer(self) -> None:
        self.app.callback()(self.typer_callback)

    def typer_callback(
        self,
        version: bool = typer.Option(
            None,
            "--version",
            "-v",
            is_eager=True,
            help="Show version",
        ),
    ) -> None:
        if version:
            typer.echo("Test version: 0.0.0")
            typer.Exit(0)
