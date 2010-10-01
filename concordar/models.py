# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt4 import QtCore, QtGui
import concordance

class BasicConcordanceServer(object):
    def concordance(self, text, word, radius, tokenized):
        return tuple(concordance.search_sequence(tokenized, word, radius))

    def tokenize(self, text):
        return concordance.import_file(text)
        
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
