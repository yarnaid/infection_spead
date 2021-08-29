from backend.config_parser import Config
from dataStructure.gRPC import Building, HumanState, BaseUnit, BuildingType
from pure_protobuf.types import int32
from itertools import count
from pure_protobuf.dataclasses_ import message, field
from dataclasses import dataclass
from typing import List

DUMMY_MAP_CONFIG_NAME = "tests/dummy_test_config.txt"
SERIALIZATION_FILE = "C:/Users/tyryk/PycharmProjects/infection_spread/tests/test_serialization.txt"
HUMANS_KEY = "serialized_humans"
BUILDINGS_KEY = "serialized_buildings"


@message
@dataclass
class ResearchMap:

    """
    Main class for map on which the mathematical model of the spread of infection is built

    Parameters:
    ----------

     config_name: str:
        Filename for reading map settings
     config_data: dict
        Attribute, that stores the map settings for building a model
     map_population: list
        List of HumanState-objects, placed on the map
     map_buildings: list
        List of Building-objects, placed on the map
     map_length: int
        Length of model Map-object
     map_width: int
        Width of model Map-object

    """

    config_name: str = field(1, default="")
    config_data: Config = field(2, default=None)
    map_length: int = field(3, default=0)
    map_width: int = field(4, default=0)
    map_population: List[HumanState] = field(5, default_factory=list)
    map_buildings: List[Building] = field(6, default_factory=list)

    def __post_init__(self):
        self.config_data = Config(self.config_name)
        self.map_length = self.config_data.map_length
        self.map_width = self.config_data.map_width

        BaseUnit.borders_indent = self.config_data.indent_from_borders
        BaseUnit.min_wall_len = self.config_data.minimal_wall_length
        BaseUnit.max_wall_len = self.config_data.map_length // self.config_data.wall_length_divider

        self.map_population = []
        self.map_buildings = []
        self.create_generation_list()
        self.create_buildings_list()

    def iter_buildings(self):

        """
        Method returning iterator of buildings, placed on map

        :return: Iterator of list with Building-objects
        """

        return iter(self.get_buildings())

    def iter_population(self):

        """
        Method returning iterator of human population units on the map

        :return: Iterator of list with HumanState-objects
        """

        return iter(self.get_population())

    def create_buildings_list(self):

        """
        Method of creating objects of buildings on the map

        :return: List of Building-objects
        """

        buildings_list = []
        buildings_quantity = self.config_data.buildings
        for i in range(buildings_quantity):
            new_building = Building.from_parameters(len(self.map_buildings) + len(self.map_population),
                                                    self.map_length, self.map_width)
            if not buildings_list:  # if there is no buildings on map
                buildings_list.append(new_building)
            else:
                iterations = count()
                while self.has_intersection(new_building)\
                        and next(iterations) < self.config_data.iteration_constraint:
                    new_building = Building.from_parameters(len(self.map_buildings) + len(self.map_population),
                                                            self.map_length, self.map_width)
                if next(iterations) < self.config_data.iteration_constraint:
                    buildings_list.append(new_building)
        self.map_buildings = buildings_list

    def create_generation_list(self):
        """
        Method for random generating population of the city

        :return: List of Human-objects
        """
        human_objects = []
        for i in range(self.config_data.population):
            human_objects.append(HumanState.
                                 human_from_parameters(len(self.map_buildings) + len(self.map_population),
                                                       self.map_length, self.map_width))
        self.map_population = human_objects

    def has_intersection(self, new_building: Building) -> bool:

        """
        Method for finding intersection between current building and already existing buildings (from list)

        :param: new_building: Building
            New with which we want to drive the intersections of other objects on the map

        :return:
            True, if new building has an intersection with at least one building from list of placed buildings,
            or False in other cases
        """

        for building in self.map_buildings:
            if new_building.intersection_check(building):
                return True
        return False

    def get_population(self):
        return self.map_population

    def get_buildings(self):
        return self.map_buildings

    # def dumps(self) -> dict:
    #
    #     """
    #     Method for serialization ResearchMap-object to byte sequence
    #
    #     :return:
    #         Sequence of bytes obtained by serializing the card
    #     """
    #
    #     serialized_buildings = []
    #     for building in self.map_buildings:
    #         building_serialized = building.dumps()
    #         serialized_buildings.append(building_serialized)
    #
    #     serialized_humans = []
    #     for human in self.map_population:
    #         human_serialized = human.dumps()
    #         serialized_humans.append(human_serialized)
    #
    #     return {"serialized_humans": serialized_humans,
    #             "serialized_buildings": serialized_buildings}
    #
    # def dump(self, filename: str) -> None:
    #
    #     """
    #     Method for serialization ResearchMap-object to file
    #
    #     Parameters:
    #     ----------
    #
    #     filename: str
    #         Serialization stream name without format
    #     """
    #
    #     with open(filename, "w") as file:
    #
    #         for human in self.map_population:
    #             human.dump(io.BytesIO(human.dumps()))
    #
    #         for building in self.map_buildings:
    #             building.dump(io.BytesIO(file))

    # @staticmethod
    # def load(filename: str) -> "ResearchMap":
    #     bytes_data = yaml.load()


def create_dummy_map() -> ResearchMap:

    """
    Method for creating dummy map for simple way of testing model
    Dummy map is 500px long and 500px wide (fixed config options), other parameters
    from config are not used in tests

    :return: ResearchMap-object with all data about model map
    """

    research_map = ResearchMap(DUMMY_MAP_CONFIG_NAME)
    hardcoded_buildings = [Building(int32(1), 108, 228, BuildingType.HOUSE, int32(72), int32(114)),
                           Building(int32(2), 76, 288, BuildingType.HOUSE, int32(72), int32(76)),
                           Building(int32(3), 396, 228, BuildingType.HOUSE, int32(108), int32(114)),
                           Building(int32(4), 288, 418, BuildingType.HOUSE, int32(72), int32(76))]
    research_map.map_buildings = hardcoded_buildings
    return research_map



