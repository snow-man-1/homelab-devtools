# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typer import Typer

from homelab_devtools.cli_factory import CliFactory
from homelab_devtools.logger_factory import LoggerFactory


def start_cli() -> None:
    LoggerFactory.setup_logger()

    factory = CliFactory()

    cli_app: Typer = factory.create_cli_app()
    cli_app()


if __name__ == "__main__":
    start_cli()
