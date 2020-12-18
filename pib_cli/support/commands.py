"""CLI Utilities"""

import os

import yaml
from pib_cli import config_filename
from .paths import PathManager
from .processes import ProcessManager


class Commands:
  overload_env_name = 'PIB_OVERLOAD_ARGUMENTS'

  def __init__(self):
    self.process_manager = ProcessManager()
    self.path_manager = PathManager()
    with open(config_filename) as file_handle:
      self.config = yaml.safe_load(file_handle)

  def __find_config_entry(self, name):
    for entry in self.config:
      if entry['name'] == name:
        return entry
    raise KeyError("Could not find yaml key name: %s" % name)

  def __add_overload(self, overload):
    if overload:
      overload_string = " ".join(overload)
      os.environ[self.__class__.overload_env_name] = overload_string

  def __translate_response(self):
    if self.process_manager.exit_code == 0:
      return 'success'
    return 'failure'

  @staticmethod
  def coerce_from_string_to_list(command):
    if isinstance(command, str):
      return [command]
    return command

  def invoke(self, command, overload=None):
    config = self.__find_config_entry(command)
    goto_path = getattr(self.path_manager, config['path_method'])
    goto_path()

    self.__add_overload(overload)

    prepared_command = self.coerce_from_string_to_list(config['commands'])
    self.process_manager.spawn(prepared_command)

    return config[self.__translate_response()]