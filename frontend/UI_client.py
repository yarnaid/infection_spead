from frontend.UI.infection_spread_ui import Ui_MainWindow
import PyQt5
import sys
import logging
import typing
from random import randint, choice, uniform

HUMAN_SIZE = 3.5  # radius of human dote


class ModelingApp(PyQt5.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, width: float, length: float) -> None:
        super().__init__()
        self.setupUi(self)
        self.resize(width, length)  # resize to map size from backend

        self.human_color = {"ILL": 'red', "NORMAL": 'blue'}  # rework when connecting with backend

        self.init_working_buttons()

        self.show()

    def init_working_buttons(self) -> None:
        self.dummyButton.clicked.connect(self.debug_draw_dummy_random_map)

    def draw_map(self, map_objects: list) -> None:

        for building in map_objects:
            self.create_building(building.coord_x, building.coord_y, building.width, building.length)

    def create_canvas(self) -> None:
        """
        Creating canvas to paint building and humans
        :return:
        """
        canvas = PyQt5.QtGui.QPixmap(self.width(), self.height())
        canvas.fill(PyQt5.QtGui.QColor('white'))
        self.canvas.setPixmap(canvas)
        self.setCentralWidget(self.canvas)

    def debug_draw_dummy_random_map(self) -> None:
        """
        Debug function to create random number of random people and buildings
        :return:
        """
        self.create_canvas()
        buildings = randint(5, 15)
        for i in range(buildings):
            self.draw_random_building()

        humans = randint(10, 50)
        for i in range(humans):
            self.draw_random_human()
        logger.info("Draw dummy random map")

    def draw_random_building(self) -> None:
        """
        Function random x,y coordinate and sizes, and call function to paint this random building
        :return:
        """
        max_y = self.height()
        max_x = self.width()
        rand_width = randint(30, 80)
        rand_length = randint(30, 80)
        rand_x = uniform(0, max_x - rand_width)
        rand_y = uniform(0, max_y - rand_length)
        self.create_building(rand_x, rand_y, rand_width, rand_length)

    def draw_random_human(self) -> None:
        """
        Function random x,y coordinate and type and call function to paint this random human
        :return:
        """
        max_y = self.height()
        max_x = self.width() - HUMAN_SIZE
        x = uniform(0, max_x)
        y = uniform(0, max_y)
        human_type = choice(list(self.human_color.keys()))
        self.create_human(x, y, human_type)

    def create_human(self, x: float, y: float, human_type: str) -> None:
        """
        Function to paint dote, representing human at modeling
        :param x: float/int:
        :param y: float/int:
        :param human_type:
        :return:
        """
        color = self.human_color[human_type]
        size = HUMAN_SIZE
        qp = PyQt5.QtGui.QPainter(self.canvas.pixmap())
        qp.begin(self)
        br = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor(color))
        qp.setBrush(br)
        qp.setPen(PyQt5.QtGui.QColor('black'))
        qp.drawEllipse(PyQt5.QtCore.QPointF(x, y), float(size), float(size))
        qp.end()
        if self.coordinateBox.isChecked():
            self.draw_coordinate(x, y)

    def draw_coordinate(self, x: float, y: float) -> None:
        """
        function to write coordinate at position
        :param x: int/float:
        :param y: int/float:
        :return:
        """
        qp = PyQt5.QtGui.QPainter(self.canvas.pixmap())
        qp.begin(self)
        qp.drawText(PyQt5.QtCore.QRectF(PyQt5.QtCore.QPointF(x, y - 10), PyQt5.QtCore.QSizeF(100, 50)),
                    PyQt5.QtCore.Qt.AlignCenter |
                    PyQt5.QtCore.Qt.AlignTop,
                    "(" + str(round(x, 2)) + "," + str(round(y, 2)) + ")")
        qp.end()

    def create_building(self, x: float, y: float, width: float, length: float) -> None:  # TODO ANGLE?
        """
        Function painting rectangle, representing building( only houses at this point)
        :param x: int/float :
        :param y: int/float :
        :param width: int/float:
        :param length: int/float:
        --------- width
        |
        |
        |
        length
        :return:
        """
        qp = PyQt5.QtGui.QPainter(self.canvas.pixmap())
        qp.begin(self)
        br = PyQt5.QtGui.QBrush(PyQt5.QtGui.QColor('grey'))
        qp.setBrush(br)
        qp.setPen(PyQt5.QtGui.QColor('black'))
        qp.drawRect(PyQt5.QtCore.QRectF(PyQt5.QtCore.QPointF(x, y), PyQt5.QtCore.QSizeF(width, length)))
        qp.end()
        if self.coordinateBox.isChecked():
            self.draw_coordinate(x, y)


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # new instance QApplication
    w_size, l_size = 800, 600
    window = ModelingApp(w_size, l_size)
    window.show()
    sys.exit(app.exec_())
