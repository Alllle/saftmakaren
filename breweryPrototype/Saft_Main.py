import Saft__MainView as SF
import sys
from PyQt5 import QtWidgets
###KLICKA INTE PÅ SAVE UTAN ATT HA SELECTAT ETT RECEPT ÄN....men om du gör det så gör om jsonfilen till backupen
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = SF.SaftApp()
    qt_app.show()
    app.exec_()

