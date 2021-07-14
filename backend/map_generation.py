from backend.config_parser import ConfigFileParser, ConfigParameters
from dataStructure.gRPC import Building, HumanState
from itertools import count
import typing


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
     map_population: list
        List of HumanState-objects, placed on the map
     map_buildings: list
        List of Building-objects, placed on the map

    """

    def __init__(self, config_name: str):
        self.config_data = ConfigFileParser(config_name).parse_config()
        self.__wall_len_limit = self.config_data[ConfigParameters.MAP_LENGTH.value]\
                                // self.config_data[ConfigParameters.WALL_LENGTH_DIVIDER.value]
        self.map_length = self.config_data[ConfigParameters.MAP_LENGTH.value]
        self.map_width = self.config_data[ConfigParameters.MAP_WIDTH.value]
        self.__map_population = []
        self.__map_buildings = []
        self.create_generation_list()
        self.create_buildings_list()

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
            new_building = Building.from_parameters(len(self.__map_buildings) + len(self.__map_population),
                                                    self.config_data[ConfigParameters.MIN_WALL_LEN.value],
                                                    self.__wall_len_limit,
                                                    self.config_data[ConfigParameters.BORDERS_INDENT.value],
                                                    self.map_length,
                                                    self.map_width)
            if not buildings_list:  # if there is no buildings on map
                buildings_list.append(new_building)
            else:
                iterations = count()
                while self.has_intersection(new_building)\
                        and next(iterations) < self.config_data[ConfigParameters.ITERATION_CONSTRAINT.value]:
                    new_building = Building.from_parameters(len(self.__map_buildings) + len(self.__map_population),
                                                            self.config_data[ConfigParameters.MIN_WALL_LEN.value],
                                                            self.__wall_len_limit,
                                                            self.config_data[ConfigParameters.BORDERS_INDENT.value],
                                                            self.map_length,
                                                            self.map_width)
                if next(iterations) < self.config_data[ConfigParameters.ITERATION_CONSTRAINT.value]:
                    buildings_list.append(new_building)
        return buildings_list

    def create_generation_list(self):
        """
        Method for random generating population of the city

        :return: List of Human-objects
        """
        human_objects = []
        for i in range(self.config_data[ConfigParameters.POPULATION_QUANTITY.value]):
            human_objects.append(HumanState.human_from_parameters(self.length(), self.width(), len(self.__map_buildings)
                                                                  + len(self.__map_population)))
        return human_objects

    def has_intersection(self, new_building: Building):

        """
        Method for finding intersection between current building and already existing buildings (from list)

        :param: new_building: Building
            New with which we want to drive the intersections of other objects on the map

        :return:
            True, if new building has an intersection with at least one building from list of placed buildings,
            or False in other cases
        """

        for building in self.__map_buildings:
            if new_building.intersection_check(building):
                return True
        return False

    def length(self):
        return self.map_length

    def width(self):
        return self.map_width

    def get_population(self):
        return self.__map_population

    def get_buildings(self):
        return self.__map_buildings
