# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt4 import QtCore
import concordance, importers

class BasicConcordanceServer(object):
    """A façade for algorithms implementing a basic concordance."""
    
    def concordance(self, word, radius, tokenized):
        """Returns a concordance for a single word to the server."""
        return tuple(concordance.search_sequence(tokenized, word, radius))

    def tokenize(self, text):
        """Returns non-punctuation, whitespace-separated tokens."""
        return importers.graphical_tokenize(text)
        
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
        """Sets the list of passages to show the user."""
        self.beginResetModel()
        self.matches = matches
        self.endResetModel()
