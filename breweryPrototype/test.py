# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 680)
        self.addRecipe = QtWidgets.QPushButton(Dialog)
        self.addRecipe.setGeometry(QtCore.QRect(190, 40, 75, 23))
        self.addRecipe.setObjectName("addRecipe")
        self.textAdd = QtWidgets.QLineEdit(Dialog)
        self.textAdd.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.textAdd.setObjectName("textAdd")
        self.recipes = QtWidgets.QListWidget(Dialog)
        self.recipes.setGeometry(QtCore.QRect(0, 0, 141, 691))
        self.recipes.setObjectName("recipes")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addRecipe.clicked.connect(self.addRecipeFunc)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addRecipe.setText(_translate("Dialog", "Add"))

    def addRecipeFunc(self):
        self.recipes.addItem('test')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


