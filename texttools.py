# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from PyQt4.QtSql import QSqlTableModel
import parsing
import ui_main_window
from index_database import create_database, create_table, insert_word

class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        concordance_db = create_database()
        settings = QSettings('Ludovico', 'Indexer')
        already_run = settings.value('run_before', 0)
        if not already_run:
            create_table(concordance_db)
            insert_word(concordance_db, 'pane', 'pane e vino', 'marcellino')
            settings.setValue('run_before', 1)
        concordanceModel =  QSqlTableModel()
        concordanceModel.setTable('words_locations')
        concordanceModel.select()
        self.setupUi(self)
        self.wordListView.setModel(concordanceModel);
        self.parser = parsing.Parser()
        
    def choose_file(self):
        self.parser.file = QtGui.QFileDialog.getOpenFileName(self, 'Choose file to import', '', '')

    def parse(self):
        pass

    def write_to_storage(self):
        pass

    def import_file(self):
        self.choose_file()
        self.parse()
        self.write_to_storage()
