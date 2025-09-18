# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typer import Typer

from homelab_devtools.cli_factory import CliFactory


def start_cli() -> None:
    factory = CliFactory()

    cli_app: Typer = factory.create_cli_app()
    cli_app()


if __name__ == "__main__":
    start_cli()
