from dataclasses import dataclass
from pure_protobuf.dataclasses_ import field, message
from pure_protobuf.types import int32
from enum import IntEnum
from typing import List


class statusCode(IntEnum):
    UNDEFINED = 0
    SUCCESS = 1
    ERROR = 2


@message
@dataclass
class Metadata:
    status: statusCode = field(1)
    request_id: int32 = field(2, default=int32(0))
    UUID: str = field(3, default="UUID")


@message
@dataclass
class BaseUnit:
    id: int32 = field(1, default=int32(0))
    coord_x: float = field(2, default=float(0))
    coord_y: float = field(3, default=float(0))

    def validation(self):
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
        msg = self.validation()
        assert not bool(msg), msg


class HealthStatus(IntEnum):
    NORMAL = 0
    ILL = 1
    RECOVERED = 2
    DEAD = 3


@message
@dataclass
class HumanState(BaseUnit):
    health_status: HealthStatus = field(1, default=HealthStatus.NORMAL)


class BuildingType(IntEnum):
    HOUSE = 0
    ROAD = 1


@message
@dataclass
class Building(BaseUnit):
    type: BuildingType = field(1, default=BuildingType.HOUSE)
    width: int32 = field(2, default=int32(0))
    length: int32 = field(3, default=int32(0))
    angle: int32 = field(4, default=int32(0))


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
