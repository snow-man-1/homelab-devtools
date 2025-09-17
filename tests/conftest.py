import pytest
from typer import Typer

from homelab_devtools.command_registry import CommandRegistry


@pytest.fixture
def command_registry() -> CommandRegistry:
    return CommandRegistry()


class MockCommand:
    def __init__(self):
        self.app = Typer()


@pytest.fixture
def mock_command() -> MockCommand:
    return MockCommand()
