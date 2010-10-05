# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from . import concordance, importers

class Cache(object):
    def __init__(self, text):
        self.set_text(text)

    def set_text(self, text):
        """Builds non-punctuation, whitespace-separated tokens."""
        self.text = text
        tokenized = importers.graphical_tokenize(text)
        self.tokens = [item.token for item in tokenized]
        self.coords = [item.coord for item in tokenized]

    
class BasicConcordanceServer(object):
    """A façade for algorithms implementing a basic concordance."""
    def __init__(self, cache):
        self.cache = cache

    def concordance(self, word, radius):
        """Returns a concordance for a single word to the server."""
        return tuple(concordance.search_sequence(self.cache.tokens, word, radius))

        
class ConcordanceModel(QtCore.QAbstractTableModel):
    """A generated concordance."""

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
