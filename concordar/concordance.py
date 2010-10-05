# -*- coding: utf-8 -*-

from PyQt4 import QtGui


def lowercase_same(word1, word2):
    """Returns whether the lowercase forms of the two words match."""
    return word1.lower() == word2.lower()
            
def search_sequence(sequence, word, width):
    """Yields matching strings and their indices."""
    for result in build_results(sequence, symmetric_ranges(matching_indices(sequence, word), width, len(sequence))):
        yield result
      
def build_results(tokens, ranges):
    """Yields index and text for relevant ranges."""
    for index, start, end in ranges:
        matches = tokens[start:end]
        yield (index,  ' '.join(matches))

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

def matching_indices(sequence, word, criterion_definition=lowercase_same):
    """Returns the indices of the matching tokens."""
    import operator
    import functools
    criterion = functools.partial(criterion_definition, word)
    return map(lambda x: operator.getitem(x, 0), filter(lambda x:criterion(x[1]), zip(range(len(sequence)),sequence)))
       
