from enum import Enum
from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class ConfigParameters(Enum):
    """
    A set of configuration options for creating qt application for the model
    """

    HUMAN_SIZE = "human_dote_size"  # radius of human dote
    RAND_MIN_BUILDING = "random_minimum_buildings"
    RAND_MAX_BUILDING = "random_maximum_buildings"
    RAND_MIN_HUMANS = "random_minimum_humans"
    RAND_MAX_HUMANS = "random_maximum_humans"
    RAND_BUILDING_SIZE_MIN = "random_building_size_minimum"
    RAND_BUILDING_SIZE_MAX = "random_building_size_maximum"


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
            processed_config.update({key: float(config.defaults().get(key))})
        return processed_config
