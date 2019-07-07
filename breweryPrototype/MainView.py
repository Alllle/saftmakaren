# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Main

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

        self.textBoxes = [self.textAdd]

        self.addRecipe.clicked.connect(self.addRecipeFunc)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addRecipe.setText(_translate("Dialog", "Add"))

    def startApplication(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = MainView()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
    # Button functions are down here
    def addRecipeFunc(self, user):
        args = list()
        for textBox in self.textBoxes:
            args.append(textBox.text())
        # AddRecipes returns the title for display at the sidebar
        title = Main.addRecipe(args)
        self.textAdd.clear()
        self.recipes.addItem(title)