from enum import Enum

CONFIG_SEPARATOR = "="


class ConfigParameters(Enum):  # a set of configuration options for creating a map for the model
    POPULATION_QUANTITY = "population"
    BUILDINGS_QUANTITY = "buildings"
    MAP_LENGTH = "map_length"
    MAP_WIDTH = "map_width"


class ConfigParser:
    __config_name = ""

    def __init__(self, config_name: str):
        ConfigParser.__config_name = config_name

    @staticmethod
    def parse_config():
        with open(ConfigParser.__config_name, "r") as f:
            config_data = f.readlines()
            model_parameters = dict()
            for param_str in config_data:
                for param in ConfigParameters:
                    if param.value in param_str:
                        param_value = int(param_str.replace(param.value, "")
                                          .replace(CONFIG_SEPARATOR, "")
                                          .replace("\n", ""))
                        # we assume that all parameters are integer for now
                        model_parameters.update({param.value: param_value})
        return model_parameters
