# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from itertools import izip, islice
import io

def make_groups(list, size):
    """
    >>> numbers = (1,2,3,)
    >>> g = make_groups(numbers, 2)
    >>> g.next()
    (1, 2)
    >>> g.next()
    (2, 3)
    """
    
    phased_iterators = [ islice(list, start, None) for start in range(size) ]
    return zip(*phased_iterators)


def words_with_context(words):
    """
    """
    word_index = {}
    for group in make_groups(words, 5):
        word_index[group[2]] = ' '.join(group)
    return word_index


def parse(text):
    return words_with_context(text.split())
