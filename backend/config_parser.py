from configparser import ConfigParser
from dataclasses import dataclass, field


@dataclass
class Config:
    """
    A class of configuration options for creating a map for the model
    """

    population: int = field(default=0)
    buildings: int = field(default=0)
    map_length: int = field(default=0)
    map_width: int = field(default=0)
    min_wall_len: int = field(default=0)
    iteration_constraint: int = field(default=0)
    borders_indent: int = field(default=0)
    wall_length_divider: int = field(default=0)

    def __init__(self, config_name: str):
        parser = ConfigParser()
        parser.read(config_name)
        for key, value in parser.defaults().items():
            if hasattr(self, key):
                attr_type = self.__annotations__.get(key)
                setattr(self, key, attr_type(value))
