# -*- coding: utf-8 -*-
from PyQt4 import QtGui

def graphical_tokenize(text):
   """Tokenizes the text using the document cursor."""
      
   def generate_list(text):

      doc = QtGui.QTextDocument(text)
      cursor = QtGui.QTextCursor(doc)
      cursor.select(QtGui.QTextCursor.WordUnderCursor)

      yield (cursor.position(), cursor.selectedText())
      while cursor.movePosition(QtGui.QTextCursor.NextWord):
         cursor.select(QtGui.QTextCursor.WordUnderCursor)

         yield (cursor.position(), cursor.selectedText())

   import itertools
   positions, words = itertools.tee(generate_list(text))
   return (tuple((item[0] for item in positions)), tuple((item[1] for item in words)))

