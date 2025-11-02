# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

import typer

from homelab_devtools.commands.base_command import BaseCommand
from homelab_devtools.decorators import as_typer_callback


class MainCommand(BaseCommand):
    @as_typer_callback
    def main(
        self,
        version: bool = typer.Option(False, "--version", "-v", help="Show version"),
    ) -> None:
        if version:
            pass
