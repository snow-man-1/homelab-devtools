# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

# Third Party Imports
import pytest
from typer.testing import CliRunner

# Project Imports
from homelab_devtools import __version__
from homelab_devtools.main import app


@pytest.fixture()
def cli_runner():
    """Create a cli runner instance to invoke typer"""
    return CliRunner()


def test_version_output(cli_runner):
    """Test that app --version returns the current version number"""
    result = cli_runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_help(cli_runner):
    """Test that the app shows a help text when no arguments are provided"""
    result = cli_runner.invoke(app)
    assert "Usage" in result.stdout
