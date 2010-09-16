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


class TextTools(QtGui.QMainWindow, ui_main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TextTools, self).__init__(parent)
        self.setupUi(self)
        self.actionImport.triggered.connect(self.choose_file)
        self.textBrowser.viewport().setCursor(QtCore.Qt.PointingHandCursor)
        self.textBrowser.cursorPositionChanged.connect(self.update_from_text)
        self.actionQuit.setShortcut(QtGui.QKeySequence.Quit)
        self.radiusBox = QtGui.QSpinBox()
        self.radiusBox.setMinimum(1)
        self.radiusBox.valueChanged.connect(self.update_from_text)
        self.toolBar.addWidget(QtGui.QLabel('Context size'))
        self.toolBar.addWidget(self.radiusBox)
       
    def choose_file(self):
        text_file = QtGui.QFileDialog.getOpenFileName(self, 'Choose file to import', '', '')
        self.import_file(text_file)

    def import_file(self, text_file):
        with open(text_file, 'r') as f:
            text = f.read()
        self.textBrowser.setPlainText(text.decode('utf-8'))

    def show_word_context(self, word, radius=2):
        import concordance
        self.matchesView.clear()
        radius = self.radiusBox.value()
        for match in concordance.search(self.textBrowser.toPlainText(), word, radius):
            self.matchesView.addItem(match)

    def update_from_text(self):
        current_cursor = self.textBrowser.textCursor()
        current_cursor.select(QtGui.QTextCursor.WordUnderCursor)
        word = current_cursor.selectedText()
        self.show_word_context(word)
          
        extra_selection = QtGui.QTextEdit.ExtraSelection()
        selected_format = QtGui.QTextCharFormat()
        selected_format.setBackground(QtGui.QBrush(QtGui.QColor('yellow')))
        extra_selection.format = selected_format
        extra_selection.cursor = current_cursor
        self.textBrowser.setExtraSelections((extra_selection,))
