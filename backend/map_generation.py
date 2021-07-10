from enum import Enum
import random as rand
from dataStructure.gRPC import HumanType
from backend.config_parser import ConfigFileParser, ConfigParameters
import datetime
from dataclasses import dataclass
from dataStructure.gRPC import Building, BaseUnit
from pure_protobuf.types import int32


class BuildingType(Enum):

    """
    Class with set of constants for the designation of building types on the map
    """

    HOSPITAL = 0
    OFFICE = 1
    HOUSE = 2
    STREET = 3

# conditionally, for now, we believe that a minimum should fit into the city along each coordinate axis
# 5 houses, so we will store the limitation on the length of the wall as a field of the map instance,
# depending on the length / width of the random card


class ResearchMap:

    def __init__(self, config_name: str):  # map object constructor for research
        self.config_data = ConfigFileParser(config_name).parse_config()
        self.__wall_len_limit = self.config_data[ConfigParameters.MAP_LENGTH.value]\
                                // 5  # why 5-written in the comment above
        self.__id_counter = 0
        self.__map_population = self.create_generation_list()  # for population keeping
        self.__map_buildings = self.create_buildings_list()  # for keeping buildings information

    def iter_buildings(self):
        for elem in self.get_buildings():
            yield elem

    def iter_population(self):
        for elem in self.get_population():
            yield elem

    def create_buildings_list(self):

        """
        Method of creating objects of buildings on the map
        :return: List of Building-objects
        """

        buildings_list = []
        buildings_quantity = self.config_data[ConfigParameters.BUILDINGS_QUANTITY.value]
        for i in range(buildings_quantity):
            new_building = ResearchMap.create_building_parameters(self.__wall_len_limit, self.config_data,
                                                                  self.__id_counter)
            if not buildings_list:  # if there is no buildings on map
                buildings_list.append(new_building)
                self.__id_counter += 1
            else:
                iterations = 0
                while ResearchMap.has_intersection(buildings_list, new_building)\
                        and iterations < self.config_data[ConfigParameters.ITERATION_CONSTRAINT.value]:
                    new_building = ResearchMap.create_building_parameters(self.__wall_len_limit, self.config_data,
                                                                          self.__id_counter)
                    iterations += 1
                if iterations < self.config_data[ConfigParameters.ITERATION_CONSTRAINT.value]:
                    buildings_list.append(new_building)
                    self.__id_counter += 1
        return buildings_list

    @staticmethod
    def create_building_parameters(wall_len_limit, config_data, id_counter):

        """
        Method for generating parameters of each building on map
        :return: Building-object, storing the geometric data of the building on the map
        """

        rand.seed(datetime.datetime.now().microsecond)
        width = rand.randint(config_data[ConfigParameters.MIN_WALL_LEN.value], wall_len_limit)
        length = rand.randint(config_data[ConfigParameters.MIN_WALL_LEN.value], wall_len_limit)
        borders_indent = config_data[ConfigParameters.BORDERS_INDENT.value]
        x = borders_indent + rand.randint(0, config_data[ConfigParameters.MAP_LENGTH.value]
                                          - length - 2 * borders_indent)
        y = borders_indent + rand.randint(0, config_data[ConfigParameters.MAP_WIDTH.value]
                                          - width - 2 * borders_indent)
        base_unit = BaseUnit(id_counter, x, y)
        angle = 0  # for now we don't use this field in map generation
        return Building(base_unit, BuildingType.HOUSE, width, length, angle)

    def create_generation_list(self):
        """
        Method for random generating population of the city
        :return: List of Human-objects
        """
        human_objects = []
        for i in range(self.config_data[ConfigParameters.POPULATION_QUANTITY.value]):
            rand.seed(datetime.datetime.now().microsecond)
            human_x = rand.triangular(0, self.get_map_length())
            human_y = rand.triangular(0, self.get_map_width())
            human_objects.append(Human(BaseUnit(self.__id_counter, human_x, human_y)))
        return human_objects

    @staticmethod
    def intersection_check(first_building, second_building):

        """
        Method for checking buildings intersections

        :param first_building: Building
        :param second_building: Building
            Two objects of class Building for to check for intersection

        :return: True, if buildings have an intersection, or False in other cases
        """

        assert isinstance(first_building, Building), "Invalid type of first input argument"
        assert isinstance(second_building, Building), "Invalid type of second input arguments"

        x_first = [first_building.base.coord_x - first_building.length / 2,
                   first_building.base.coord_x + first_building.length / 2]
        y_first = [first_building.base.coord_y - first_building.width / 2,
                   first_building.base.coord_y + first_building.width / 2]

        x_second = [second_building.base.coord_x - second_building.length / 2,
                    second_building.base.coord_x + second_building.length / 2]
        y_second = [second_building.base.coord_y - second_building.width / 2,
                    second_building.base.coord_y + second_building.width / 2]

        return max(x_first) < min(x_second) or max(y_first) < min(y_second) or min(y_first) > max(y_second)

    @staticmethod
    def has_intersection(buildings_list, new_building):

        """
        Method for finding intersection between new building and already existing buildings

        :param buildings_list: list
            List of Building-objects, which keeps all building, already placed on the map
        :param new_building:
            New Building-object to be placed on the map
        :return:
            True, if new building has an intersection with at least one building from list of placed buildings,
            or False in other cases
        """

        for building in buildings_list:
            if ResearchMap.intersection_check(building, new_building):
                return True
        return False

    def get_map_length(self):
        return self.config_data[ConfigParameters.MAP_LENGTH.value]

    def get_map_width(self):
        return self.config_data[ConfigParameters.MAP_WIDTH.value]

    def get_population(self):
        return self.__map_population

    def get_buildings(self):
        return self.__map_buildings


@dataclass
class Human:
    """
    Population unit class

    Parameters:
    -----------
        __base: BaseUnit
            Class, which keeps x and y coordinate of human dote
        __human_type: HumanType
            type of person in infectious research
    """
    __base: BaseUnit
    __human_type: HumanType = HumanType.NORMAL
