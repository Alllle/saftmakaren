import Saft__MainView as SF
import sys
from PyQt5 import QtWidgets
###KLICKA INTE PÅ SAVE UTAN ATT HA SELECTAT ETT RECEPT ÄN....men om du gör det så gör om jsonfilen till backupen.
#tror alla problem har att göra med att objektet "current user" är mutable, och när man skickar objektet till rf.RecepieFactory.SaveUser(currentUser)
# så gör man först om det till dict för att kunna spara som json, och då förändras
#även orginal objektet(tror jag).
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = SF.SaftApp()
    qt_app.show()
    app.exec_()

