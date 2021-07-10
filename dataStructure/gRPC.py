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


class HumanType(IntEnum):
    NORMAL = 0
    ILL = 1
    RECOVERED = 2
    DEAD = 3


@message
@dataclass
class HumanState:
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
