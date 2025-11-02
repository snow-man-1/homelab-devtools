# SPDX-License-Identifier: MIT
"""
Author: snow-man-1
"""

import logging
from collections.abc import Generator
from typing import Any

import pytest

from homelab_devtools.cli_factory import CliFactory
from homelab_devtools.commands.base_command import BaseCommand
from homelab_devtools.decorators import as_typer_command
from homelab_devtools.errors import BusinessLogicError, ExternalError, InputError
from homelab_devtools.logger_factory import LoggerFactory


@pytest.fixture
def cli_factory() -> CliFactory:
    return CliFactory()


class MockTyper:
    def __init__(self):
        self.registered_commands = []

    def command(self, name=None):
        def decorator(method):
            mock_typer_command = MockTyperCommand(method, name or method.__name__)
            self.registered_commands.append(mock_typer_command)
            return mock_typer_command

        return decorator

    def add_typer(self, typer):
        pass


class MockTyperCommand:
    def __init__(self, method, name):
        self.name = name
        self.method = method

    def __call__(self, *args, **kwds):
        return self.method(*args, **kwds)


@pytest.fixture
def mock_typer() -> MockTyper:
    typer_mock = MockTyper()
    return typer_mock


class MockCommand(BaseCommand):
    def __init__(self, command_group, app=None):
        super().__init__(command_group, app)

    @as_typer_command
    def test(self):
        return

    def test_with_user_input_error(self):
        raise InputError("Test with user input error")

    def test_with_business_logic_error(self):
        raise BusinessLogicError("Test with business logic error")

    def test_with_external_error(self):
        raise ExternalError("Test with external error")

    def test_with_unexpected_error(self):
        raise Exception("Test with unexpected Error")


@pytest.fixture
def mock_command(mock_typer: Any) -> BaseCommand:
    mock_command = MockCommand("mock", app=mock_typer)
    return mock_command


@pytest.fixture
def logger_factory() -> Generator[LoggerFactory, None, None]:
    reset_logger_factory()
    yield LoggerFactory
    reset_logger_factory()


def reset_logger_factory():
    LoggerFactory._setup_finished = False
    logging.getLogger().handlers.clear()
