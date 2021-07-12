import random as rand
from backend.config_parser import ConfigFileParser, ConfigParameters
import datetime
from dataStructure.gRPC import Building, HumanState, HealthStatus, BuildingType
from pure_protobuf.types import int32


class ResearchMap:

    """
    Main class for map on which the mathematical model of the spread of infection is built

    Parameters:
    ----------

     config_data: dict
        Attribute, that stores the map settings for building a model
     wall_len_limit: int
        Limit of walls of buildings, placed on current map (conditionally, for now, we believe that a minimum should fit
        into the city along each coordinate axis 5 houses,
        so we will store the limitation on the length of the wall as a field of the map instance,
        depending on the length / width of the random card)
     id_counter: int
        Counter of objects (Buildings or HumanStates) on the map
     map_population: list
        List of HumanState-objects, placed on the map
     map_buildings: list
        List of Building-objects, placed on the map

    """

    __wall_length_divider = 5

    def __init__(self, config_name: str):
        self.config_data = ConfigFileParser(config_name).parse_config()
        self.__wall_len_limit = self.config_data[ConfigParameters.MAP_LENGTH.value] // ResearchMap.__wall_length_divider
        self.__id_counter = 0
        self.__map_population = self.create_generation_list()
        self.__map_buildings = self.create_buildings_list()

    def generator_buildings(self):

        """
        Method returning iterator of buildings, placed on map

        :return: Iterator of list with Building-objects
        """

        return iter(self.get_buildings())

    def generator_population(self):

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
        x = borders_indent + rand.triangular(0, config_data[ConfigParameters.MAP_LENGTH.value]
                                             - length - 2 * borders_indent)
        y = borders_indent + rand.triangular(0, config_data[ConfigParameters.MAP_WIDTH.value]
                                             - width - 2 * borders_indent)
        angle = int32(0)  # for now we don't use this field in map generation
        return Building(id_counter, x, y, BuildingType.HOUSE, int32(width), int32(length), int32(angle))

    def create_generation_list(self):
        """
        Method for random generating population of the city

        :return: List of Human-objects
        """
        human_objects = []
        for i in range(self.config_data[ConfigParameters.POPULATION_QUANTITY.value]):
            rand.seed(datetime.datetime.now().microsecond)
            human_x = rand.triangular(0, self.length())
            human_y = rand.triangular(0, self.width())
            human_objects.append(HumanState(int32(self.__id_counter), human_x, human_y, HealthStatus.NORMAL))
        return human_objects

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
            if Building.intersection_check(building, new_building):
                return True
        return False

    def length(self):
        return self.config_data[ConfigParameters.MAP_LENGTH.value]

    def width(self):
        return self.config_data[ConfigParameters.MAP_WIDTH.value]

    def get_population(self):
        return self.__map_population

    def get_buildings(self):
        return self.__map_buildings
