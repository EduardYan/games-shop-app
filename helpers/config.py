"""
Some utils functions
to use for the configuration.

"""

from json import load


class ConfigFileInvalid(ValueError):
	"""
	Model for the execption in case
	the config file is invalid.
	"""
	pass



def validate_config_object(object:dict) -> bool:
	"""
	Return True or False if the keys
	in the config object passed for
	parameter are valid.
	"""

	allow_keys = [
		'PORT',
	]

	for key in allow_keys:
		if key not in object:
			raise ConfigFileInvalid('The config file is invalid, verify the keys and values.')


def get_config_object() -> dict:
	"""
	Return a dictionary with the
	configuration set in json file 'config.json'.
	"""

	# path for file
	CONFIG_PATH = './config.json'
	CONFIG_FILE = open(CONFIG_PATH, 'r')

	object = load(CONFIG_FILE)

	return object


# config object to use
CONFIG = get_config_object()
validate_config_object(CONFIG)
