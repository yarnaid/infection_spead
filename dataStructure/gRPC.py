from dataclasses import dataclass
from pure_protobuf.dataclasses_ import field, message
from pure_protobuf.types import int32
from enum import IntEnum

# gRPC_status_creator = {'UNDEFINED': 0, 'SUCCESS': 1, 'ERROR': 2}  # Dont know how to do it better
# gRPC_human_types = {'NORMAL': 0, 'ILL': 1, 'RECOVERED': 2, 'DEAD': 3}
# gRPC_building_types = {'HOUSE': 0, 'ROAD': 1}


class RequestCounter:  # counter of unique request id
    id = 0

    @staticmethod
    def give_id():
        RequestCounter.id += 1
        return RequestCounter.id


# TODO EMPLEMENT ALL HERE. REWORKED.
class statusCode(IntEnum):
    UNDEFINED = 0
    SUCCESS = 1
    ERROR = 2


@message
@dataclass
class Metadata:
    status: statusCode = field(1)
    request_id: int32 = field(2, default=int32(0))
    UUID: str = field(3)


@message
@dataclass
class BaseUnit:
    id: int32 = field(1, default=int32(0))
    coord_x: int32 = field(2, default=int32(0))
    coord_y: int32 = field(3, default=int32(0))


class HumanType(IntEnum):
    NORMAL = 0
    ILL = 1
    RECOVERED = 2
    DEAD = 3


@message
@dataclass
class State:
    base: BaseUnit = field(1)
    type: HumanType = field(2)


class BuildingType(IntEnum):
    HOUSE = 0
    ROAD = 1


@message
@dataclass
class Building:
    base: BaseUnit = field(1)
    type: BuildingType = field(2)
    width: int32 = field(3)
    length: int32 = field(4)
    angle: int32 = field(5)


@message
@dataclass
class Map:
    meta: Metadata = field(1)
    building: Building = field(2)


@message
@dataclass
class UpdateResponse:
    meta: Metadata = field(1)
    state: State = field(2)
