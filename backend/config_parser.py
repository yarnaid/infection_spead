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


class ConfigFileParser(ConfigParser):
    __config_name = ""
    __section_name = ""

    def __init__(self, config_name: str, section_name: str):
        super().__init__()
        ConfigFileParser.__config_name = config_name
        ConfigFileParser.__section_name = section_name

    @staticmethod
    def parse_config():
        config = ConfigParser()
        config.read(ConfigFileParser.__config_name)
        return config[ConfigFileParser.__section_name]


