from gui import GraphicalUI
from PyQt5 import QtWidgets


class Main:

    GraphicalUI()

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = GraphicalUI()
        ui.ui_setup(Form)
        Form.show()
        sys.exit(app.exec_())


