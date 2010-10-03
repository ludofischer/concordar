# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt4 import QtGui


def lowercase_extractor(word):
    def configured_extractor(index, match):
        if match.lower() == word.lower():
            return index

    return configured_extractor

def search_sequence(sequence, word, width):
   for result in build_results(sequence, symmetric_ranges(positions(sequence, word), width, len(sequence))):
      yield result
      
def build_results(sequence, ranges):
   for index, start, end in ranges:
      words = [item[2] for item in sequence[start:end]]
      yield (sequence[index][1], ' '.join(words))

def symmetric_ranges(iterable, width, maximum):
    for index in iterable:
        if index - width < 0:
            start = 0
        else:
            start = index - width

        if index + width + 1 > maximum:
            end = maximum
        else:
            end = index + width + 1
        yield (index, start, end)

def positions(sequence, word, criterion_definition=lowercase_extractor):
    matches_criterion = criterion_definition(word)
    return [matches_criterion(index, thing) for (index, coord, thing) in sequence]
       

