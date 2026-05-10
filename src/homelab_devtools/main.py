# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

# Third Party
import typer

# Project imports
from homelab_devtools import __version__
from homelab_devtools.logger_factory import LoggerFactory

app: typer.Typer = typer.Typer(
    add_completion=False,
    help="Homelab Devtools - Help managing your Homelab",
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        is_eager=True,
        help="Show version",
    ),
) -> None:
    if version:
        typer.echo(f"Version: {__version__}")
        raise typer.Exit(0)

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


def start_cli() -> None:
    LoggerFactory.setup_logger()
    app()


if __name__ == "__main__":
    start_cli()
