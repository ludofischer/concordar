# -*- coding: utf-8 -*-

#    copyright 2010 Ludovico Fischer

#    This file is part of Concordance.
#
#    Concordance is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Concordance is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Concordance.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from PyQt4 import QtCore, QtGui

import ui_main_window
import models

class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        self.construct_layout()
        self.connect_slots()
        self.setup_interactive_concordance()

    def construct_layout(self):
        self.setupUi(self)
        self.actionQuit.setShortcut(QtGui.QKeySequence.Quit)
        self.actionOpen.setShortcut(QtGui.QKeySequence.Open)
        
        self.textBrowser.viewport().setCursor(QtCore.Qt.PointingHandCursor)
        palette = self.textBrowser.palette()
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor('cyan'))
        palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor('black'))
        self.textBrowser.setPalette(palette)
        self.radiusBox = QtGui.QSpinBox()
        self.radiusBox.setMinimum(1)
        self.wordField = QtGui.QLineEdit()
        self.wordField.setMaximumWidth(200)
        self.toolBar.addWidget(QtGui.QLabel(self.tr('Word:')))
        self.toolBar.addWidget(self.wordField)
        spacer = QtGui.QWidget(self)
        spacer.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.toolBar.addWidget(spacer)
        self.toolBar.addWidget(QtGui.QLabel(self.tr('Context size:')))
        self.toolBar.addWidget(self.radiusBox)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
       
    def connect_slots(self):
        self.actionOpen.triggered.connect(self.choose_file)
        self.textBrowser.cursorPositionChanged.connect(self.new_word_selected_in_text)
        self.radiusBox.valueChanged.connect(self.update_concordance)
        self.wordField.textEdited.connect(self.new_word_typed)
        self.matchesView.clicked.connect(self.move_cursor_to_word)

    def setup_interactive_concordance(self):
        self.concordanceModel = models.ConcordanceModel()
        self.matchesView.setModel(self.concordanceModel)
        self.matchesView.setModelColumn(1)
        self.server = models.BasicConcordanceServer()
        self.text = self.textBrowser.toPlainText()
        self.tokenized = self.server.tokenize(self.text)

    def choose_file(self):
        text_file = QtGui.QFileDialog.getOpenFileName(self, self.tr('Choose file to import'), QtCore.QDir.homePath(), self.tr('Text files (*.txt)'))
        self.change_working_file(text_file)

    def change_working_file(self, text_file):
        with open(text_file, 'r') as f:
            text = f.read().decode('utf-8')
        self.text = text
        self.tokenized = self.server.tokenize(text)
        self.prepare_browser()

    def prepare_browser(self):
        self.textBrowser.blockSignals(True)
        self.textBrowser.setPlainText(self.text)
        self.textBrowser.blockSignals(False)

    def move_cursor_to_word(self, index):
        model = index.model()
        word_position = model.data(model.index(index.row(), 0))

        
        cursor = self.textBrowser.textCursor()
      
        cursor.setPosition(word_position)
        cursor.select(QtGui.QTextCursor.WordUnderCursor)
       
        self.textBrowser.blockSignals(True)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.centerCursor()
        
        self.textBrowser.blockSignals(False)


    def new_word_selected_in_text(self):
        current_cursor = self.textBrowser.textCursor()
        current_cursor.select(QtGui.QTextCursor.WordUnderCursor)
        self.highlight_selected_word(current_cursor)
        self.word = current_cursor.selectedText()
        self.wordField.setText(self.word)
        self.update_concordance()

    def new_word_typed(self, word):
        self.word = word
        self.update_concordance()

    def highlight_selected_word(self, cursor):
        extra_selection = QtGui.QTextEdit.ExtraSelection()
        selected_format = QtGui.QTextCharFormat()
        selected_format.setBackground(QtGui.QBrush(QtGui.QColor('yellow')))
        extra_selection.format = selected_format
        extra_selection.cursor = cursor
        self.textBrowser.setExtraSelections((extra_selection,))

    def update_concordance(self):
        self.concordanceModel.set_matches(self.server.concordance(self.text, self.word, self.radiusBox.value(), self.tokenized ))

