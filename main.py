import Gui
from Gui import Ui_MainWindow
from Login import Login
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
retAtt = ui.retInputs()
sys.exit(app.exec_())