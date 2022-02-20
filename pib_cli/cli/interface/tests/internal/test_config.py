"""Test the click CLI config command interfaces."""

from pib_cli.cli.commands import config_show, config_where
from pib_cli.cli.interface.builtins import config
from pib_cli.cli.interface.tests.fixtures import cli_harness


class TestConfigShowInterface(cli_harness.CliCommandTestHarness):
  """Test the click CLI config show command interface."""

  cli_command_string = "@pib config show"
  cli_command_class = config_show.ConfigShowCommand
  cli_command_module = config


class TestConfigWhereInterface(cli_harness.CliCommandTestHarness):
  """Test the click CLI config where command interface."""

  cli_command_string = "@pib config where"
  cli_command_class = config_where.ConfigWhereCommand
  cli_command_module = config