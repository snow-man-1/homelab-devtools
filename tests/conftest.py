# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

from typing import Any, cast

import pytest
from pytest_mock import MockerFixture
from typer import Typer

from homelab_devtools.cli_factory import CliFactory


@pytest.fixture
def cli_factory() -> CliFactory:
    return CliFactory()


@pytest.fixture
def mock_typer(mocker: MockerFixture) -> Any:
    return cast(Typer, mocker.MagicMock(spec=Typer))


@pytest.fixture
def mock_command(mocker: MockerFixture, mock_typer: Any) -> MockerFixture:
    mocker.app = mock_typer
    return mocker
