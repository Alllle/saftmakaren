from PyQt5 import QtWidgets

import Saftmakaren



class SaftApp(Saftmakaren.Ui_MainWindow, QtWidgets.QMainWindow):
    #det som körs i början när man startar programmet
    def __init__(self):
        super(SaftApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()#öppnar i fullscreen
        self.setWindowTitle("Saftmakaren") #på window står det stringen
       




