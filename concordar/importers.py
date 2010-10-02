# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PyQt4 import QtGui

def import_file(text):
   def generate_list(text):
      doc = QtGui.QTextDocument(text)
      cursor = QtGui.QTextCursor(doc)
      cursor.select(QtGui.QTextCursor.WordUnderCursor)
      yield (cursor.position(), cursor.selectedText())
      while cursor.movePosition(QtGui.QTextCursor.NextWord):
         cursor.select(QtGui.QTextCursor.WordUnderCursor)
         yield (cursor.position(), cursor.selectedText())
   
   return tuple(generate_list(text))

