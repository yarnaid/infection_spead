from __future__ import annotations
from backend.config_parser import Config
from dataStructure.gRPC import Building, HumanState, BaseUnit
from itertools import count
import typing


class ResearchMap:

    """
    Main class for map on which the mathematical model of the spread of infection is built

    Parameters:
    ----------

     config_data: dict
        Attribute, that stores the map settings for building a model
     map_population: list
        List of HumanState-objects, placed on the map
     map_buildings: list
        List of Building-objects, placed on the map

    """

    def __init__(self, config_name: str):
        self.config_data = Config(config_name)

        # BaseUnit.borders_indent = self.config_data.indent_from_borders
        # BaseUnit.min_wall_len = self.config_data.minimal_wall_length
        # BaseUnit.max_wall_len = self.config_data.map_length // self.config_data.wall_length_divider

        self.map_population = []
        self.map_buildings = []
        self.map_population = self.create_generation_list()
        self.map_buildings = self.create_buildings_list()

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

    def create_buildings_list(self) -> typing.List[Building]:

        """
        Method of creating objects of buildings on the map

        :return: List of Building-objects
        """

        buildings_list: typing.List[Building] = []
        buildings_quantity = self.config_data.buildings
        for i in range(buildings_quantity):
            new_building = Building.from_parameters(
                len(self.map_buildings) + len(self.map_population),
                self.config_data.map_length,
                self.config_data.map_width,
            )
            if not buildings_list:  # if there is no buildings on map
                buildings_list.append(new_building)
            else:
                iterations = count()
                while self.has_intersection(new_building) and next(iterations) < self.config_data.iteration_constraint:
                    new_building = Building.from_parameters(
                        len(self.map_buildings) + len(self.map_population),
                        self.config_data.map_length,
                        self.config_data.map_width,
                    )
                if next(iterations) < self.config_data.iteration_constraint:
                    buildings_list.append(new_building)
        return buildings_list

    def create_generation_list(self) -> typing.List[HumanState]:
        """
        Method for random generating population of the city

        :return: List of Human-objects
        """
        human_objects: typing.List[HumanState] = []
        for _ in range(self.config_data.population):
            human_objects.append(
                HumanState.human_from_parameters(
                    len(self.map_buildings) + len(self.map_population),
                    self.config_data.map_length,
                    self.config_data.map_width,
                )
            )
        return human_objects

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
