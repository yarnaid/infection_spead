import pytest
from dataStructure.gRPC import Building, BuildingType
from pure_protobuf.types import int32
from backend.config_parser import Config
from backend.map_generation import DUMMY_MAP_CONFIG_NAME, create_dummy_map

# tests for basic research map functions
no_intersection_test = [Building(int32(1), float(30), float(30), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                        Building(int32(2), float(60), float(60), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                        False,
                        "Test, when rectangles have no intersection"]

has_intersection_test = [Building(int32(3), float(30), float(40), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                         Building(int32(4), float(60), float(70), BuildingType.HOUSE, int32(60), int32(60), int32(0)),
                         True,
                         "Test, when rectangles have an intersection" "Test, when rectangles have no intersection"]

test_examples = [has_intersection_test, no_intersection_test]


@pytest.mark.parametrize('test_data', test_examples, ids=str)
def test_intersection_check(test_data: Building) -> None:
    first_building, second_building, answer, *_ = test_data
    assert Building.intersection_check(first_building, second_building) == answer


def test_dummy_map():
    buildings = [Building(int32(1), 108, 228, BuildingType.HOUSE, int32(72), int32(114)),
                 Building(int32(2), 76, 288, BuildingType.HOUSE, int32(72), int32(76)),
                 Building(int32(3), 396, 228, BuildingType.HOUSE, int32(108), int32(114)),
                 Building(int32(4), 288, 418, BuildingType.HOUSE, int32(72), int32(76))]

    dummy_map_parameters = Config(DUMMY_MAP_CONFIG_NAME).__dict__

    test_map = create_dummy_map()

    for building_required, building_created in zip(buildings, test_map.map_buildings):
        assert building_required.coord_x == building_created.coord_x
        assert building_required.coord_y == building_created.coord_y
        assert building_required.type == building_created.type
        assert building_required.length == building_created.length
        assert building_required.width == building_created.width

    for key in test_map.config_data.__dict__.keys():
        assert dummy_map_parameters[key] == test_map.config_data.__getattribute__(key)
