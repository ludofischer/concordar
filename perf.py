from __future__ import unicode_literals
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from concordar import importers

with open('samples/moby_dick.txt', 'r') as f:
    text = f.read()

sequence = importers.import_file(text)
"""
positions = tuple(alternate.positions(sequence, 'the'))

ranges = tuple(alternate.build_ranges(positions, 1, len(positions)))

word_groups = tuple(alternate.get_word_groups(sequence, ranges))

def tuplize(thing):
    return tuple(thing)

def lister(match):
    return [item[1] for item in match]

def search(thing):
    for coord, match in thing:
        words = lister(tuplize(match))
        yield(coord, ' '.join(words))

searched = tuple(search(word_groups))
"""
