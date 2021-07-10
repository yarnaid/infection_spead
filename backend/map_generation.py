from enum import Enum
import random as rand
import math
from dataStructure.gRPC import HumanType
from config_parser import ConfigParser, ConfigParameters
import datetime
from dataclasses import dataclass


class BuildingType(Enum):  # a set of constants for the designation of building types on the map
    HOSPITAL = 0
    OFFICE = 1
    HOUSE = 2
    STREET = 3

# conditionally, for now, we believe that a minimum should fit into the city along each coordinate axis
# 5 houses, so we will store the limitation on the length of the wall as a field of the map instance,
# depending on the length / width of the random card


MIN_WALL_LEN = 10  # minimal wall length value

ITERATION_CONSTRAINT = 1000  # restriction on iterations in building a city map
INDENT_FROM_BORDERS = 3  # indent from city borders


class ResearchMap:

    def __init__(self, config_name: str):  # map object constructor for research
        self.config_data = ConfigParser(config_name).parse_config()
        self.__wall_len_limit = self.config_data.get(
            ConfigParameters.MAP_WIDTH.value) // 5  # why 5-written in the comm above
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
        buildings_quantity = self.config_data.get(ConfigParameters.BUILDINGS_QUANTITY.value)
        for i in range(buildings_quantity):
            new_building = ResearchMap.create_building_parameters(self.__wall_len_limit, self.config_data)
            if not buildings_list:  # if there is no buildings on map
                buildings_list.append(new_building)
            else:
                iterations = 0
                while ResearchMap.has_intersection(buildings_list, new_building)\
                        and iterations < ITERATION_CONSTRAINT:
                    new_building = ResearchMap.create_building_parameters(self.__wall_len_limit, self.config_data)
                    iterations += 1
                if iterations < ITERATION_CONSTRAINT:
                    buildings_list.append(new_building)
        return buildings_list

    @staticmethod
    def create_building_parameters(wall_len_limit, config_data: dict):

        """
        Method for generating parameters of each building on map
        :return: Building-object, storing the geometric data of the building on the map
        """

        rand.seed(datetime.datetime.now().microsecond)
        width = rand.randint(MIN_WALL_LEN, wall_len_limit)
        length = rand.randint(MIN_WALL_LEN, wall_len_limit)
        x = INDENT_FROM_BORDERS + rand.randint(0, config_data.get(ConfigParameters.MAP_LENGTH.value)
                                               - length - 2 * INDENT_FROM_BORDERS)
        y = INDENT_FROM_BORDERS + rand.randint(0, config_data.get(ConfigParameters.MAP_WIDTH.value)
                                               - width - 2 * INDENT_FROM_BORDERS)
        angle = 0  # for now we don't use this field in map generation
        return Building(x, y, width, length, angle)

    def create_generation_list(self):
        """
        Method for random generating population of the city
        :return: List of Human-objects
        """
        human_objects = []
        for i in range(self.config_data.get(ConfigParameters.POPULATION_QUANTITY.value)):
            rand.seed(datetime.datetime.now().microsecond)
            human_x = rand.triangular(0, self.get_map_length())
            human_y = rand.triangular(0, self.get_map_width())
            human_objects.append(Human(human_x, human_y))
        return human_objects

    @staticmethod
    def intersection_check(first_building, second_building):

        """
        Method for checking buildings intersections

        :param first_building: Building
        :param second_building: Building
            Two objects of class Building for to check for intersection

        :return: True, if buildings have intersection, or False in other cases
        """

        if not isinstance(first_building, Building) or not isinstance(second_building, Building):
            return False  # while we handle the error of object types in this way
        semi_length_1 = first_building.get_length() / 2
        semi_width_1 = first_building.get_width() / 2

        semi_length_2 = second_building.get_length() / 2
        semi_width_2 = second_building.get_width() / 2

        x_1 = first_building.get_x()
        y_1 = first_building.get_y()

        x_2 = second_building.get_x()
        y_2 = second_building.get_y()

        if math.fabs(x_2 - x_1) <= math.fabs(semi_length_1 - semi_length_2):
            return True
        elif math.fabs(y_2 - y_1) <= math.fabs(semi_width_1 - semi_width_2):
            return True
        return False  # returns True, if current buildings have an intersection

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
        return self.config_data.get(ConfigParameters.MAP_LENGTH.value)

    def get_map_width(self):
        return self.config_data.get(ConfigParameters.MAP_WIDTH.value)

    def get_population(self):
        return self.__map_population

    def get_buildings(self):
        return self.__map_buildings


@dataclass
class Building:

    """
    City building class

    Parameters:
    -----------
        __x: float
            x coordinate of center of the building on map
        __y: float
            y coordinate of center of the building on map
        __length: float
            the size of the building along the x-axis
        __width: float
            the size of the building along the y-axis
        __angle: float
            the angle of deviation of the building from the horizontal position

    Methods:
    -------
        get_length()
            Returns the size of the building along the x-axis
        get_width()
            Returns the size of the building along the y-axis
        get_x()
            Returns x coordinate of center of the building
        get_y()
            Returns y coordinate of center of the building
    """

    __x: float
    __y: float
    __width: float
    __length: float
    __angle: float = 0

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


@dataclass
class Human:
    """
    Population unit class

    Parameters:
    -----------
        __x: float
            x coordinate of human dote
        __y: float
            y coordinate of human dote
        __human_type: HumanType
            type of person in infectious research
    """
    __x: float
    __y: float
    __human_type: HumanType = HumanType.NORMAL
