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
        self.concordanceModel =  QSqlTableModel()
        self.concordanceModel.setTable('words_locations')
        self.concordanceModel.select()
        self.setupUi(self)
        self.wordListView.setModel(self.concordanceModel);
        self.parser = parsing.Parser()
        self.actionImport.triggered.connect(self.choose_file)

    def choose_file(self):
        text = QtGui.QFileDialog.getOpenFileName(self, 'Choose file to import', '', '')
        self.import_file(text)

    def write_to_storage(self, parsed):
        pass

    def import_file(self, text):
        parsed_stuff = self.parser.parse(text)
        self.write_to_storage(parsed_stuff)
