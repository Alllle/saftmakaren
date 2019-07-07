# The main file connecting different parts of the program
import View

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = View.MainView()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())