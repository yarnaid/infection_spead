from dataclasses import dataclass
from pure_protobuf.dataclasses_ import field, message
from pure_protobuf.types import int32
from enum import IntEnum
from typing import List


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

    def get_building_bounds(self):

        """
        Method for getting all 4 bounds of a building to further find intersections with other buildings

        :return: Dictionary, which keeps left and right bounds of building along the x and y axes
        """

        x_bounds = [self.coord_x - self.length / 2,
                    self.coord_x + self.length / 2]
        y_bounds = [self.coord_y - self.width / 2,
                    self.coord_y + self.width / 2]
        return dict({'x': x_bounds, 'y': y_bounds})


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
