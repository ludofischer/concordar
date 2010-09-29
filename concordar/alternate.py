# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from concordance import lowercase_extractor

def import_file(text):
   def generate_list(text):
      doc = QtGui.QTextDocument(text)
      cursor = QtGui.QTextCursor(doc)
      cursor.select(QtGui.QTextCursor.WordUnderCursor)
      while cursor.movePosition(QtGui.QTextCursor.NextWord):
         cursor.select(QtGui.QTextCursor.WordUnderCursor)
         yield (cursor.position(), cursor.selectedText())
   
   return tuple(generate_list(text))

def remove_punctuation(position_words):
   def is_alphanumeric(position, word):
      import re
#      return re.compile('\w', re.UNICODE).match

def positions(sequence, word, criterion_definition=lowercase_extractor):
    matches_criterion = criterion_definition(word)
    for (position, thing) in sequence:
        if matches_criterion(thing):
            yield position, thing

def search_sequence(sequence, word):
   for position, match in positions(sequence, word):
      pass
