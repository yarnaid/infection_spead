from enum import Enum
from configparser import ConfigParser


class ConfigParameters(Enum):  # a set of configuration options for creating a map for the model
    POPULATION_QUANTITY = "population"
    BUILDINGS_QUANTITY = "buildings"
    MAP_LENGTH = "map_length"
    MAP_WIDTH = "map_width"
    MIN_WALL_LEN = "minimal_wall_length"
    ITERATION_CONSTRAINT = "iteration_constraint"
    BORDERS_INDENT = "indent_from_borders"
    WALL_LENGTH_DIVIDER = "wall_length_divider"


class ConfigFileParser(ConfigParser):
    __config_name = ""

    def __init__(self, config_name: str):
        super().__init__()
        ConfigFileParser.__config_name = config_name

    @staticmethod
    def parse_config():
        config = ConfigParser()
        config.read(ConfigFileParser.__config_name)
        processed_config = dict()
        for key in config.defaults().keys():
            processed_config.update({key: int(config.defaults().get(key))})
        return processed_config


