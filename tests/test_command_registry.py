import typer
from pytest_mock import MockerFixture

from homelab_devtools.command_registry import CommandRegistry


class TestCommandRegistry:
    """
    The command registry should have the following behaviour:
    1. it is a module singleton
    2. at start there are no typer instances registered
    3. at startup the registry is used to instanciate a primary typer instance which is filled with all command typer instances
    4. each command class has it's own typer instance which will be added to the main one when creating an app
    """

    def test_registry_can_create_cli_app(self, command_registry: CommandRegistry):
        cli_instance: typer.Typer = command_registry.create_cli_app()
        assert isinstance(cli_instance, typer.Typer)

    def test_registry_can_register_command(
        self, command_registry: CommandRegistry, mock_command: MockerFixture
    ):
        command_registry.register("mock", mock_command.app)
        assert isinstance(command_registry.get_command("mock"), typer.Typer)

    def test_get_command_returns_none_at_beginning(
        self, command_registry: CommandRegistry
    ):
        assert command_registry.get_command("mock") is None
