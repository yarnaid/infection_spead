from frontend.echo_client import run_get_map
from frontend.UI_client import ModelingApp
import sys


class ModelingShower:
    def __init__(self):
        self.res_map = run_get_map()
        self.app = QtWidgets.QApplication(sys.argv)  # new instance QApplication
        self.window = ModelingApp()
        self.window.show()
        self.get_and_show_map()
        sys.exit(self.app.exec_())

    def get_and_show_map(self):
        self.window.collect_map(self.res_map)


shower = ModelingShower()
