# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import collections

def graphical_tokenize(text):
   """Tokenizes the text using the document cursor."""
   Coord = collections.namedtuple('Coord', 'coord token')
   def generate_list(text):
      
      doc = QtGui.QTextDocument(text)
      cursor = QtGui.QTextCursor(doc)
      cursor.select(QtGui.QTextCursor.WordUnderCursor)

      yield Coord(cursor.position(), cursor.selectedText())
      while cursor.movePosition(QtGui.QTextCursor.NextWord):
         cursor.select(QtGui.QTextCursor.WordUnderCursor)

         yield Coord(cursor.position(), cursor.selectedText())


   return tuple(generate_list(text))

