# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from concordance import lowercase_extractor, numerize

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
    
def build_ranges(iterable, width, maximum):
    for index, coord in iterable:
        if index - width < 0:
            start = 0
        else:
            start = index - width

        if index + width + 1 > maximum:
            end = maximum
        else:
            end = index + width + 1
        yield (coord, start, end)

def positions(sequence, word, criterion_definition=lowercase_extractor):
    matches_criterion = criterion_definition(word)
    for (index, (coord, thing)) in numerize(sequence):
        if matches_criterion(thing):
            yield (index, coord)


def get_word_groups(sequence, ranges):
    from itertools import islice
    for coord, start, end in ranges:
        yield (coord, islice(sequence, start, end))

def search_sequence(sequence, word, width):
   from itertools import islice
   for coord, match in get_word_groups(sequence, build_ranges(positions(sequence, word), width, len(sequence))):
      words = [item[1] for item in match]
      yield(coord, ' '.join(words))
