# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt4 import QtGui


def lowercase_extractor(word):
    def configured_extractor(match):
        return match.lower() == word.lower()
    return configured_extractor

def search_sequence(sequence, word, width):
   for result in build_results(sequence, symmetric_ranges(positions(sequence, word), width, len(sequence))):
      yield result
      
def build_results(sequence, ranges):
   for index, start, end in ranges:
      words = [item[1] for item in sequence[start:end]]
      yield (sequence[index][0], ' '.join(words))

def get_word_groups(sequence, ranges):
    for index, start, end in ranges:
        yield (index, sequence[start:end])

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
    for (index, (coord, thing)) in numerize(sequence):
        if matches_criterion(thing):
            yield index


def numerize(sequence):
    from future_builtins import zip
    return zip(range(len(sequence)), sequence)
