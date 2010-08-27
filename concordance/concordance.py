# -*- coding: utf-8 -*-

#    copyright 2010 Ludovico Fischer

#    This file is part of Concordance.
#
#    Concordance is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Concordance is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Concordance.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import unicode_literals
from future_builtins import zip
from itertools import islice
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
    >>> words = ('cane', 'gatto', 'olio', 'corda', 'tavolo', 'orto')
    >>> words_with_context(words).next()
    ('olio', u'cane gatto olio corda tavolo')
    """
    for group in make_groups(words, 5):
        yield (group[2], ' '.join(group),)
  


def parse(text):
    return words_with_context(text.split())
