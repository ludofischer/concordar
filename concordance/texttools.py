# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
from PyQt4.QtSql import QSqlTableModel
import concordance
import ui_main_window
from index_database import create_database, create_table, insert_word, retrieve_contexts

class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        self.concordance_db = create_database()
        settings = QSettings('Ludovico', 'Indexer')
        already_run = int(settings.value('run_before', 0))
        if not already_run:
            create_table(self.concordance_db)
            insert_word(self.concordance_db, (('pane','pane e vino'),), 'marcellino')
            settings.setValue('run_before', 1)
        self.concordanceModel =  QSqlTableModel()
        self.concordanceModel.setTable('words_locations')
        self.concordanceModel.select()
        self.setupUi(self)
        self.wordListView.setModel(self.concordanceModel);
        self.actionImport.triggered.connect(self.choose_file)
        self.wordListView.clicked.connect(self.show_word_context)

    def choose_file(self):
        text_file = QtGui.QFileDialog.getOpenFileName(self, 'Choose file to import', '', '')
        self.import_file(text_file)

    def write_to_storage(self, parsed):
        insert_word(self.concordance_db, parsed, 'default')

    def import_file(self, text_file):
        with io.open(text_file, 'r') as f:
            text = f.read()
        parsed_stuff = concordance.parse(text)
        self.write_to_storage(parsed_stuff)
        self.concordanceModel.select()
        self.textBrowser.setText(text)

    def show_word_context(self, model_index):
        record = self.concordanceModel.record(model_index.row())
        text = '\n'.join(retrieve_contexts(self.concordance_db, record.value(0)))
        self.textBrowser.setText(text)
            
        

