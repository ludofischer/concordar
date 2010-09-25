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

def extract(iterable, criterion):
    for (number, word) in iterable:
        if criterion(word):
            yield number
    
    
def build_groups(iterable, width, maximum):
    for number in iterable:
        if number - width < 0:
            start = 0
        else:
            start = number - width

        if number + width + 1 > maximum:
            end = maximum
        else:
            end = number + width + 1
        yield (start, end)

def get_words(sequence, groups):
    from itertools import islice
    for group in groups:
        yield islice(sequence, *group)

def get_formatted_words(sequence, groups):
    for match in get_words(sequence, groups):
        yield ' '.join(match)
    
def search_sequence(sequence, word, width):
    return get_formatted_words(sequence, build_groups(extract(numerize(sequence), lowercase_extractor(word)),width, len(sequence)))
