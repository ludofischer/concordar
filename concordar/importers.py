# -*- coding: utf-8 -*-

from PyQt4 import QtGui

def graphical_tokenize(text):
   """Tokenizes the text using the document cursor."""

   def generate_list(text):
      doc = QtGui.QTextDocument(text)
      cursor = QtGui.QTextCursor(doc)
      cursor.select(QtGui.QTextCursor.WordUnderCursor)
      index = 0
      yield (index, cursor.position(), cursor.selectedText())
      while cursor.movePosition(QtGui.QTextCursor.NextWord):
         cursor.select(QtGui.QTextCursor.WordUnderCursor)
         index += 1
         yield (index, cursor.position(), cursor.selectedText())
   
   return tuple(generate_list(text))

