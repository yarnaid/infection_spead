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


