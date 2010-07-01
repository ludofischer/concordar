import sys
from PyQt4 import QtCore, QtGui
import ui_main_window
from PyQt4.QtSql import QSqlTableModel

class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        concordanceModel =  QSqlTableModel()
        concordanceModel.setTable('words_locations')
        concordanceModel.select()
        self.wordListView.setModel(concordanceModel);
        self.setupUi(self)
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    text_tools = TextTools()
    text_tools.show()
    app.exec_() 
