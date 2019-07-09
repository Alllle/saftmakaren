from PyQt5 import QtWidgets

import Saftmakaren, sys


class SaftApp(Saftmakaren.Ui_MainWindow, QtWidgets.QMainWindow):
    #det som körs i början när man startar programmet
    def __init__(self):
        super(SaftApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()#öppnar i fullscreen
        self.setWindowTitle("Saftmakaren") #på window står det stringen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = SaftApp()
    qt_app.show()
    app.exec_()


