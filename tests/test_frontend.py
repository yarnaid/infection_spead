import pytest
from frontend import UI_client, UI_config_parser


@pytest.fixture(autouse=True)
def init_window(qtbot):
    window = UI_client.ModelingApp()
    qtbot.addWidget(window)
    qtbot.wait_for_window_shown(window)
    return window


@pytest.mark.usefixtures('init_window')
class Test_UI:
    def test_create_rnd_human(self, qtbot, init_window):  # test creating random Human dote
        rand_hum = init_window.create_random_human()
        assert type(rand_hum) == UI_client.HumanDote  # this is HumanDote class
        assert rand_hum.type in UI_client.HUMAN_COLORS.keys()  # human have valid type
        assert rand_hum.x > 0  # valid coordinate

    def test_create_rnd_building(self, qtbot, init_window):  # test creating random Building
        rand_building = init_window.create_random_building()
        assert type(rand_building) == UI_client.BuildingRectangle  # we expect Building Rect
        assert rand_building.width > 0  # valid coord

    def test_create_dummy_map(self, qtbot, init_window):  # test creating dummy map
        init_window.dummyButton.click()
        assert len(init_window.humans) >= UI_client.config_data[UI_config_parser.ConfigParameters.RAND_MIN_HUMANS.value]
        # we get at least min  expected amount of human
        assert len(init_window.buildings) > 0  # we get at least 1 building
        for human in init_window.humans:
            assert human.x > 0  # valid
            assert human.type in UI_client.HUMAN_COLORS.keys()  # exist type
