import pytest
from backend.map_generation import ResearchMap
from dataStructure.gRPC import Building, BaseUnit, BuildingType
from pure_protobuf.types import int32

no_intersection_test = [Building(BaseUnit(int32(1), 30, 30), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                        Building(BaseUnit(int32(2), 60, 60), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                        False,
                        "Test, when rectangles have no intersection"]

has_intersection_test = [Building(BaseUnit(int32(3), 30, 40), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
                         Building(BaseUnit(int32(4), 60, 70), BuildingType.HOUSE, int32(60), int32(60), int32(0)),
                         True,
                         "Test, when rectangles have an intersection" "Test, when rectangles have no intersection"]

test_examples = [has_intersection_test, no_intersection_test]


@pytest.mark.parametrize('test_data', test_examples, ids=str)
def test_intersection_check(test_data: Building) -> None:
    first_building = test_data[0]
    second_building = test_data[1]
    answer = test_data[2]
    assert ResearchMap.intersection_check(first_building, second_building) == answer
