# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typing import Any, cast

import pytest
from pytest_mock import MockerFixture
from typer import Typer

from homelab_devtools.cli_factory import CliFactory
from homelab_devtools.commands.base_command import BaseCommand
from homelab_devtools.decorators import as_typer_command


@pytest.fixture
def cli_factory() -> CliFactory:
    return CliFactory()


@pytest.fixture
def mock_typer(mocker: MockerFixture) -> Any:
    return cast(Typer, mocker.MagicMock(spec=Typer))


class MockCommand(BaseCommand):
    def __init__(self, command_group, app=None):
        super().__init__(command_group, app)

    @as_typer_command
    def test(self):
        return


@pytest.fixture
def mock_command(mock_typer: Any) -> BaseCommand:
    mock_command = MockCommand("mock", app=mock_typer)
    return mock_command
