# -*- coding: utf-8 -*-

from __future__ import unicode_literals

def lowercase_extractor(word):
    def configured_extractor(match):
        return match.lower() == word.lower()
    return configured_extractor

def build_list(text):
    import re
    from future_builtins import filter
    return tuple(filter(lambda x: x!= '', re.compile('\W', re.UNICODE).split(text)))


def numerize(sequence):
    from future_builtins import zip
    return zip(range(len(sequence)), sequence)

def positions(sequence, word, criterion_definition=lowercase_extractor):
    matches_criterion = criterion_definition(word)
    for (position, thing) in numerize(sequence):
        if matches_criterion(thing):
            yield position
    
def build_ranges(iterable, width, maximum):
    for number in iterable:
        if number - width < 0:
            start = 0
        else:
            start = number - width

        if number + width + 1 > maximum:
            end = maximum
        else:
            end = number + width + 1
        yield (number, (start, end))

def get_word_groups(sequence, ranges):
    from itertools import islice
    for position, group in ranges:
        yield (position, islice(sequence, *group))

    
def search_sequence(sequence, word, width):
    for position, match in get_word_groups(sequence, build_ranges(positions(sequence, word),width, len(sequence))):
        yield (position, ' '.join(match))
