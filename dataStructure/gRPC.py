from dataclasses import dataclass
from pure_protobuf.dataclasses_ import field, message
from pure_protobuf.types import int32
from enum import IntEnum
from typing import List
import random as rand
import datetime


class StatusCode(IntEnum):
    UNDEFINED = 0
    SUCCESS = 1
    ERROR = 2


@message
@dataclass
class Metadata:
    status: StatusCode = field(1)
    request_id: int32 = field(2, default=int32(0))
    UUID: str = field(3, default="UUID")


@message
@dataclass
class BaseUnit:

    """
    Base class of all features on the map, storing a unique identifier and a set of coordinates on a plane that denotes
     a point (the center of a circle representing a unit of the population,
      or the center of a rectangle representing a building)

    Parameters:
    ----------

        id: int32
            Unique identificator of each object on the map
        coord_x: float
            Field with coordinate along the x-axis
        coord_y: float
            Field with coordinate along the y-axis

    """

    id: int32 = field(1, default=int32(0))
    coord_x: float = field(2, default=float(0))
    coord_y: float = field(3, default=float(0))

    def validation(self):

        """
        Main method for checking the correctness of the types of objects passed to the constructor

        :return: Error message or empty string, if all attributes correspond to the required types
        """

        msg = ""
        for field_name, field_def in self.__dataclass_fields__.items():
            actual_type = type(getattr(self, field_name))
            # so far this is a stub, looking for a solution how to make getattr return the correct int32 instead of int
            if actual_type.__name__ == 'int':
                actual_type = int32
            if actual_type != field_def.type:
                msg = "Invalid type of input field {0} : got {1} instead of {2}"\
                    .format("\'" + field_name + "\'", "\'" + actual_type.__name__ + "\'",
                            "\'" + field_def.type.__name__ + "\'")
                break
        return msg

    def __post_init__(self):

        """
        Method for checking types of objects passed to the class constructor

        :return: Error message, if method validation() returns non-empty string with error information
        """

        msg = self.validation()
        assert not bool(msg), msg


class HealthStatus(IntEnum):

    """
    Enum class for storing a set of health statuses of people in a population

    """

    NORMAL = 0
    ILL = 1
    RECOVERED = 2
    DEAD = 3


@message
@dataclass
class HumanState(BaseUnit):

    """
    Class for keeping all information about human on the map: coordinates in two dimensions and health status

    :param: health_status: HealthStatus
        Information about current human health
    """

    health_status: HealthStatus = field(1, default=HealthStatus.NORMAL)

    @staticmethod
    def human_from_parameters(map_length: int, map_width: int, id_counter: int):

        """
        Method for random generating human with given parameters

        :param map_length: int32
            Length of map along the x-axis
        :param map_width: int32
            Length of map along the y-axis
        :param id_counter: int32
            Unique identifier of each object on model map
        :return:
            Randomly generated object of Human-class
        """

        human_x = rand.triangular(0, map_length)
        human_y = rand.triangular(0, map_width)
        return HumanState(int32(id_counter), human_x, human_y, HealthStatus.NORMAL)


class BuildingType(IntEnum):

    """
    Enum class for storing a set of building types on the map

    """

    HOUSE = 0
    ROAD = 1


@message
@dataclass
class Building(BaseUnit):

    """
    Class for keeping all information about bulding on the map: coordinates of center in two dimensions,
     length, width and angle of deviation from the x-axis

    :param: type: BuildingType
        Type of current building
    :param: width: int32
        Length of building along the y-axis
    :param: length: int32
        Length of building along the x-axis
    :param: angle: int32
        Angle of deviation from the x-axis

    """

    type: BuildingType = field(1, default=BuildingType.HOUSE)
    width: int32 = field(2, default=int32(0))
    length: int32 = field(3, default=int32(0))
    angle: int32 = field(4, default=int32(0))

    def __post_init__(self):
        """
        Method for getting all 4 bounds of a building to further find intersections with other buildings
        (attributes 'x_bounds' and 'y_bounds' are private so that it is not possible
        to change them after creating the Building-object)

        """
        self.x_bounds = [self.coord_x - self.length / 2,
                         self.coord_x + self.length / 2]
        self.y_bounds = [self.coord_y - self.width / 2,
                         self.coord_y + self.width / 2]

    def intersection_check(self, second_building):

        """
        Method for checking buildings intersections

        :param second_building: Building
            Object with which you want to check the intersection

        :return: True, if buildings have an intersection, or False in other cases
        """

        assert isinstance(second_building, Building), Building.get_assert_msg(2, second_building, Building)

        first_bounds = [self.x_bounds, self.y_bounds]
        second_bounds = [second_building.x_bounds, second_building.y_bounds]

        if max(second_bounds[0]) >= max(first_bounds[0]) or max(second_bounds[1]) >= max(first_bounds[1]):
            return max(first_bounds[0]) >= min(second_bounds[0]) \
                   and max(first_bounds[1]) >= min(second_bounds[1])
        else:
            return max(second_bounds[0]) >= min(first_bounds[0]) \
                   and max(second_bounds[1]) >= min(first_bounds[1])

    @staticmethod
    def get_assert_msg(arg_number, obj, expected_type):

        """

        Helper method for generating error message to signal the user in the rest of the program

        :param arg_number: int
            Number of attribute passed to the method from which this function is called
        :param obj:
            Object, whose type you want to check
        :param expected_type:
            Required type of passed object obj

        :return:
            A message string containing the attribute numbers, the type of the passed object, and the desired type
        """

        "Invalid type of first input argument {0}: got {1} instead of {2}".format(arg_number, obj.__class__.__name__,
                                                                                  expected_type.__name__)

    @staticmethod
    def from_parameters(id_counter: int32, min_wall_len: int, wall_len_limit: int,
                        borders_indent: int, map_length: int, map_width: int):

        """
        Method for generating random building for ap with passed parameters

        :param: id_counter: int32
            Unique identifier for new building on the map
        :param: min_wall_len: int32
            Left limit of wall length on current map
        :param: wall_len_limit: int32
            Right limit of wall length on current map
        :param: borders_indent: int32
            Indent of buildings from borders on map
        :param: map_length: int32
        :param: map_width: int32

        :return: Building-object, storing the geometric data of the building on the map
        """

        width = rand.randint(min_wall_len, wall_len_limit)
        length = rand.randint(min_wall_len, wall_len_limit)
        x = borders_indent + rand.triangular(0, map_length
                                             - length - 2 * borders_indent)
        y = borders_indent + rand.triangular(0, map_width
                                             - width - 2 * borders_indent)
        angle = int32(0)  # for now we don't use this field in map generation
        return Building(id_counter, x, y, BuildingType.HOUSE, int32(width), int32(length), int32(angle))


@message
@dataclass
class Map:
    meta: Metadata = field(1)
    map_size_w: float = field(2)
    map_size_h: float = field(3)
    building: List[Building] = field(4, default_factory=list)


@message
@dataclass
class UpdateResponse:
    meta: Metadata = field(1)
    state: List[HumanState] = field(2, default_factory=list)


@message
@dataclass
class UpdateRequest:
    meta: Metadata = field(1)
