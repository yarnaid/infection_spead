import pytest
from backend.map_generation import ResearchMap
from dataStructure.gRPC import Building, BuildingType
from pure_protobuf.types import int32
from dataclasses import dataclass
from backend.config_parser import Config


@dataclass
class Case:
    name: str
    test_num: int
    input: str
    expected: dict


def create_intersection_tests() -> list:
    """
    Method for creating tests data for checking method "intersection_check" in Building-class

    :return: list of examples with test data for checking intersection
    """
    no_intersection_test = [
        Building(int32(1), float(30), float(30), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
        Building(int32(2), float(60), float(60), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
        False,
        "Test, when rectangles have no intersection"]

    has_intersection_test = [
        Building(int32(3), float(30), float(40), BuildingType.HOUSE, int32(20), int32(20), int32(0)),
        Building(int32(4), float(60), float(70), BuildingType.HOUSE, int32(60), int32(60), int32(0)),
        True,
        "Test, when rectangles have an intersection" "Test, when rectangles have no intersection"]

    return [has_intersection_test, no_intersection_test]


def create_config_tests() -> list:
    """
    Method creating test data for checking creating Config-objects for ResearchMap

    :return: list of examples with test data
    """
    config_names = ["tests/test_backend_config_1.txt", "tests/test_backend_config_2.txt"]

    expected_data_configs = [{"map_length": 500, "map_width": 500, "buildings": 4, "population": 2,
                              "minimal_wall_length": 10, "iteration_constraint": 1000, "indent_from_borders": 3,
                              "wall_length_divider": 5},
                             {"map_length": 400, "map_width": 300, "buildings": 6, "population": 20,
                              "minimal_wall_length": 20, "iteration_constraint": 500, "indent_from_borders": 5,
                              "wall_length_divider": 2}]

    config_test_names = ["№1 test config parser", "№2 test config parser"]

    test_examples_config = []
    idx = 0
    for name, init_input, expected in zip(config_test_names, config_names, expected_data_configs):
        test_examples_config.append(Case(name=name,
                                         test_num=idx,
                                         input=init_input,
                                         expected=expected))
        idx += 1
    return test_examples_config


@pytest.mark.parametrize('test_data', create_intersection_tests(), ids=str)
def test_intersection_check(test_data: list) -> None:

    """
    Method for running intersection tests with "pytest"

    :param test_data: list
        List of data, which keeps information about test name, input and expected answer

    :return: Output information about processing tests in console
    """

    first_building, second_building, answer, *_ = test_data
    assert Building.intersection_check(first_building, second_building) == answer


@pytest.mark.parametrize('test_data', create_config_tests(), ids=str)
def test_config_parser(test_data: Case) -> None:

    """
    Method for running config generation tests with "pytest"

    :param test_data: list
        List of data, which keeps information about test name, input and expected answer

    :return: Output information about processing tests in console
    """

    config_object = Config(test_data.input)
    for key, elem in test_data.expected.items():
        assert elem == config_object.__getattribute__(key)
