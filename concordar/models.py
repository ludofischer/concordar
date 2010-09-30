# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt4 import QtCore, QtGui
import concordance
import alternate

class Server(object):
    def __init__(self):
        self.text = ''
        self.tokenized = None
    def set_text(self, text):
        self.text = text
        self.tokenized = None

    def give_basic_concordance(self, word, radius):
        if not self.tokenized:
            self.tokenized = alternate.import_file(self.text)
        return tuple(alternate.search_sequence(self.tokenized, word, radius))

class TextModel(QtCore.QAbstractListModel):
    def __init__(self, text):
        QtCore.QAbstractListModel.__init__(self)
        self.words = concordance.build_list(text)
    
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.words)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return self.words[index.row()]
        else:
            return None

class ConcordanceModel(QtCore.QAbstractTableModel):
    def __init__(self, matches=tuple(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.matches = matches

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.matches)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 2

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return self.matches[index.row()][index.column()]
        else:
            return None

    def set_matches(self, matches):
        self.beginResetModel()
        self.matches = matches
        self.endResetModel()
