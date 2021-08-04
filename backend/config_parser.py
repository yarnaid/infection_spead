from configparser import ConfigParser
from dataclasses import dataclass, field


@dataclass
class Config:

    """
    A class of configuration options for creating a map for the model

    Parameters:
    ----------

    population: int
        Quantity of people dots, placed on model map
    buildings: int
        Quantity of buildings, placed on model map
    map_length: int
        Model map length along x-axis
    map_width: int
        Model map length along y-axis
    minimal_wall_length: int
        Minimal length of each wall of each building on model map
    iteration_constraint: int
        Maximum number of iterations allowed in the building generation algorithm
    indent_from_borders: int
        Minimal indent from city borders of each building on map
    wall_length_divider: int
        Wall length divider to keep building dimensions to map scale
    """

    population: int = field(default=0)
    buildings: int = field(default=0)
    map_length: int = field(default=0)
    map_width: int = field(default=0)
    minimal_wall_length: int = field(default=0)
    iteration_constraint: int = field(default=0)
    indent_from_borders: int = field(default=0)
    wall_length_divider: int = field(default=0)

    def __init__(self, config_name: str):
        parser = ConfigParser()
        parser.read(config_name)
        for key, value in parser.defaults().items():
            if hasattr(self, key):
                attr_type = self.__annotations__.get(key)
                setattr(self, key, attr_type(value))
