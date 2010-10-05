# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt4 import QtGui


def lowercase_extractor(word):
    """Returns a function returning the index of any matching token."""
    def configured_extractor(match):
        return match.lower() == word.lower()
            
    return configured_extractor

def search_sequence(sequence, word, width):
    """Yields matching strings and their visual positioning."""
    for result in build_results(sequence, symmetric_ranges(matching_indices(sequence, word), width, len(sequence))):
        yield result
      
def build_results(sequence, ranges):
    """Yields visual position and corresponding string for ranges in sequence."""
    for index, start, end in ranges:
        words = [item[2] for item in sequence[start:end]]
        yield (sequence[index][1], ' '.join(words))

def symmetric_ranges(iterable, width, maximum):
    """Returns ranges of the specified width for iterable."""
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

def matching_indices(sequence, word, criterion_definition=lowercase_extractor):
    """Returns the indices of the matching tokens."""
    import operator
    criterion = criterion_definition(word)
    return map(lambda x: operator.getitem(x, 0), filter(lambda x: criterion(x[1]), [(index, thing) for (index, coord, thing) in sequence]))
       

