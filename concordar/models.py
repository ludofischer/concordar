# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from PyQt4 import QtCore, QtGui
from . import concordance

class TextModel(QtCore.QAbstractListModel):
    def __init__(self, text):
        super(TextModel, self).__init__()
        self.words = concordance.build_list(text)
    
    def rowCount(self):
        return len(self.words)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self.words[index]

class ConcordanceModel(QtCore.QAbstractTableModel):
    def __init__(self, matches):
        super(ConcordanceModel, self).__init__()
        self.matches = matches

    def rowCount(self):
        return len(self.matches)

    def columnCount(self):
        return 2

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self.matches[index.row()][index.column()]

    def set_matches(self, matches):
        self.beginResetModel()
        self.matches = matches
        self.endResetModel()
