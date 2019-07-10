import Saft__MainView as SF
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = SF.SaftApp()
    qt_app.show()
    app.exec_()

