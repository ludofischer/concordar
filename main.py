import sip
sip.setapi('QVariant', 2)

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import QSqlTableModel
import ui_main_window
from index_database import create_database, create_table, insert_word

class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        concordance_db = create_database()
        create_table(concordance_db)
        insert_word(concordance_db, 'pane', 'pane e vino', 'marcellino')
        concordanceModel =  QSqlTableModel()
        concordanceModel.setTable('words_locations')
        concordanceModel.select()
        self.setupUi(self)
        self.wordListView.setModel(concordanceModel);
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    text_tools = TextTools()
    text_tools.show()
    app.exec_() 
