from typing import List
from frontend.UI_config_parser import ConfigParameters, ConfigFileParser
from frontend.UI.infection_spread_ui import Ui_MainWindow
import PyQt5
import sys
import logging
import typing
from random import randint, choice, uniform

# These parameters not in config because they are more vital for  UI.
CONFIG_NAME = "frontend/UI_config.txt"
CANVAS_COLOR = 'white'
PEN_COLOR = 'black'  # color of border of object
HOUSE_COLOR = 'grey'
COORDINATE_TEXT_OFFSET = 10  # so it easy to link a coordinate and an object
COORDINATE_W = 100
COORDINATE_L = 50
HUMAN_COLORS = {"ILL": 'red', "NORMAL": 'blue'}
DEFAULT_ANGLE = 0


class BaseUnit:
    """
    This class main purpose to unify future improvements to our objects
    """

    def draw(self, MainWindow: PyQt5.QtWidgets.QMainWindow) -> None:
        raise NotImplementedError


class HumanDote(BaseUnit):
    def __init__(self, x: float, y: float, human_type: str) -> None:
        self.x = x
        self.y = y
        self.type = human_type

    def draw(self, MainWindow: PyQt5.QtWidgets.QMainWindow) -> None:
        """
        Function to paint dote, representing human
        :param MainWindow:
        :return:
        """
        color = HUMAN_COLORS[self.type]
        size = config_data[ConfigParameters.HUMAN_SIZE.value]
        qp = PyQt5.QtGui.QPainter(MainWindow.canvas.pixmap())
        qp.begin(MainWindow)
        br = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(color))
        qp.setBrush(br)
        qp.setPen(PyQt5.QtGui.QColor(PEN_COLOR))
        qp.drawEllipse(PyQt5.QtCore.QPointF(self.x, self.y), float(size), float(size))
        qp.end()


class BuildingRectangle(BaseUnit):
    def __init__(self, x: float, y: float, width: float, length: float, angle: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.angle = angle

    def draw(self, MainWindow: PyQt5.QtWidgets.QMainWindow) -> None:
        """
        Function painting rectangle, representing building(only houses at this point)
        :param MainWindow:
        :return:
        (*) --------- width
        |
        |
        |
            length
        where (*) position of rectangle
        """
        qp = PyQt5.QtGui.QPainter(MainWindow.canvas.pixmap())
        qp.begin(MainWindow)
        br = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(HOUSE_COLOR))
        qp.setBrush(br)
        qp.setPen(PyQt5.QtGui.QColor(PEN_COLOR))
        qp.drawRect(PyQt5.QtCore.QRectF(PyQt5.QtCore.QPointF(self.x, self.y),
                                        PyQt5.QtCore.QSizeF(self.width, self.length)))
        qp.end()


class ModelingApp(PyQt5.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, width: float, length: float) -> None:
        super().__init__()
        self.setupUi(self)
        self.resize(width, length)  # resize to map size from backend

        self.human_colors = HUMAN_COLORS  # rework when connecting with backend

        self.init_working_buttons()

        self.humans = []
        self.buildings = []
        self.show()

    def init_working_buttons(self) -> None:
        self.dummyButton.clicked.connect(self.debug_draw_dummy_random_map)

    def create_canvas(self) -> None:
        """
        Creating canvas to paint building and humans
        :return:
        """
        canvas = PyQt5.QtGui.QPixmap(self.width(), self.height())
        canvas.fill(PyQt5.QtGui.QColor(CANVAS_COLOR))
        self.canvas.setPixmap(canvas)
        self.setCentralWidget(self.canvas)

    def debug_draw_dummy_random_map(self) -> None:
        """
        Debug function to create random number of random people and buildings
        :return:
        """
        try:
            self.create_canvas()
            buildings = randint(config_data[ConfigParameters.RAND_MIN_BUILDING.value],
                                config_data[ConfigParameters.RAND_MAX_BUILDING.value])
            for i in range(buildings):
                building = self.create_random_building()
                building.draw(self)
                self.draw_coordinate(building.x, building.y)
                self.buildings.append(building)
            logger.info("Dummy: Create and draw buildings")
            humans = randint(config_data[ConfigParameters.RAND_MIN_HUMANS.value],
                             config_data[ConfigParameters.RAND_MAX_HUMANS.value])
            for i in range(humans):
                human = self.create_random_human()
                human.draw(self)
                self.draw_coordinate(human.x, human.y)
                self.humans.append(human)
            logger.info("Dummy: Create and draw humans")
            logger.info("Draw dummy random map")
        except Exception as ex:
            print(ex)

    def create_random_building(self) -> BuildingRectangle:
        """
        Function random x,y coordinate and sizes, and call function to paint this random building
        :return:
        """
        max_y = self.height()
        max_x = self.width()
        rand_width = randint(config_data[ConfigParameters.RAND_BUILDING_SIZE_MIN.value],
                             config_data[ConfigParameters.RAND_BUILDING_SIZE_MAX.value])
        rand_length = randint(config_data[ConfigParameters.RAND_BUILDING_SIZE_MIN.value],
                              config_data[ConfigParameters.RAND_BUILDING_SIZE_MAX.value])
        rand_x = uniform(0, max_x - rand_width)
        rand_y = uniform(0, max_y - rand_length)
        return BuildingRectangle(rand_x, rand_y, rand_width, rand_length, DEFAULT_ANGLE)

    def create_random_human(self) -> HumanDote:
        """
        Function random x,y coordinate and type and call function to paint this random human
        :return:
        """
        max_y = self.height() - config_data[ConfigParameters.HUMAN_SIZE.value]
        max_x = self.width() - config_data[ConfigParameters.HUMAN_SIZE.value]
        x = uniform(0, max_x)
        y = uniform(0, max_y)
        human_type = choice(list(HUMAN_COLORS.keys()))
        return HumanDote(x, y, human_type)

    def draw_coordinate(self, x: float, y: float) -> None:
        """
        function to write coordinate at position
        :param x: int/float:
        :param y: int/float:
        :return:
        """
        if not self.coordinateBox.isChecked():
            return
        qp = PyQt5.QtGui.QPainter(self.canvas.pixmap())
        qp.begin(self)
        qp.drawText(PyQt5.QtCore.QRectF(PyQt5.QtCore.QPointF(x - COORDINATE_TEXT_OFFSET, y - COORDINATE_TEXT_OFFSET),
                                        PyQt5.QtCore.QSizeF(COORDINATE_W, COORDINATE_L)),
                    PyQt5.QtCore.Qt.AlignCenter |
                    PyQt5.QtCore.Qt.AlignTop,
                    "(" + str(round(x, 2)) + "," + str(round(y, 2)) + ")")
        qp.end()


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
config_data = ConfigFileParser(config_name=CONFIG_NAME).parse_config()
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # new instance QApplication
    w_size, l_size = 800, 600  # ONLY FOR DEBUG
    window = ModelingApp(w_size, l_size)
    window.show()
    sys.exit(app.exec_())
