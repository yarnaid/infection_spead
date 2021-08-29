from configparser import ConfigParser
from dataclasses import dataclass
from pure_protobuf.dataclasses_ import field, message


@message
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

    config_name: str = field(1, default=0)
    population: int = field(2, default=0)
    buildings: int = field(3, default=0)
    map_length: int = field(4, default=0)
    map_width: int = field(5, default=0)
    minimal_wall_length: int = field(6, default=0)
    iteration_constraint: int = field(7, default=0)
    indent_from_borders: int = field(8, default=0)
    wall_length_divider: int = field(9, default=0)

    def __post_init__(self):
        parser = ConfigParser()
        parser.read(self.config_name)
        for key, value in parser.defaults().items():
            if hasattr(self, key):
                attr_type = self.__annotations__.get(key)
                setattr(self, key, attr_type(value))
