from frontend.UI.infection_spread_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QRectF, QPoint, QSizeF, QPointF
import sys
import logging
from random import randint, choice, uniform

HUMAN_SIZE = 3.5  # radius of human dote


class ModelingApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, width, length):
        super().__init__()
        self.setupUi(self)
        self.resize(width, length)  # resize to map size from backend

        self.human_color = {"ILL": 'red', "NORMAL": 'blue'}  # rework when connecting with backend

        self.init_working_buttons()

        self.show()

    def init_working_buttons(self):
        self.dummyButton.clicked.connect(self.debug_draw_dummy_random_map)

    def create_canvas(self):
        """
        Creating canvas to paint building and humans
        :return:
        """
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QtGui.QColor('white'))
        self.canvas.setPixmap(canvas)
        self.setCentralWidget(self.canvas)

    def debug_draw_dummy_random_map(self):
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

    def draw_random_building(self):
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

    def draw_random_human(self):
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

    def create_human(self, x, y, human_type):
        """
        Function to paint dote, representing human at modeling
        :param x: float/int : x coordinate of human dote
        :param y: float/int : y coordinate of human dote
        :param human_type: str: Human type at modeling process
        :return:
        """
        color = self.human_color[human_type]
        size = HUMAN_SIZE
        qp = QPainter(self.canvas.pixmap())
        qp.begin(self)
        br = QtGui.QBrush(QtGui.QColor(color))
        qp.setBrush(br)
        qp.setPen(QtGui.QColor('black'))
        qp.drawEllipse(QPointF(x, y), float(size), float(size))
        qp.end()
        if self.coordinateBox.isChecked():
            self.draw_coordinate(x, y)

    def draw_coordinate(self, x, y):
        """
        :param x: int/float: x coordinate of where we will write coordinates
        :param y: int/float: y coordinate of where we will write coordinates
        :return:
        """
        qp = QPainter(self.canvas.pixmap())
        qp.begin(self)
        qp.drawText(QRectF(QPointF(x, y - 10), QSizeF(100, 50)), Qt.AlignCenter | Qt.AlignTop,
                    "(" + str(round(x,2)) + "," + str(round(y,2)) + ")")
        qp.end()

    def create_building(self, x, y, width, length):
        """
        Function painting rectangle, representing building( only houses at this point)
        :param x: int/float : x coordinate of building rectangle
        :param y: int/float : y coordinate of building rectangle
        :param width: int/float:
        :param length: int/float:
        --------- width
        |
        |
        |
        length
        :return:
        """
        qp = QPainter(self.canvas.pixmap())
        qp.begin(self)
        br = QtGui.QBrush(QtGui.QColor('grey'))
        qp.setBrush(br)
        qp.setPen(QtGui.QColor('black'))
        qp.drawRect(QRectF(QPointF(x, y), QSizeF(width, length)))
        qp.end()
        if self.coordinateBox.isChecked():
            self.draw_coordinate(x, y)


logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # new instance QApplication
    w_size, l_size = 800, 600
    window = ModelingApp(w_size, l_size)
    window.show()
    sys.exit(app.exec_())
