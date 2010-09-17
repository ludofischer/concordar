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


def make_groups(listing, size):
    from itertools import islice, izip_longest
    """
    >>> numbers = (1,2,3,4)
    >>> g = make_groups(numbers, 1)
    >>> g.next()
    (1, 2, 3)
    >>> g.next()
    (2, 3, 4)
    """
    padded = ['' for i in range(size)]
    padded.extend(listing)
   
    phased_iterators = [ islice(padded, start, None) for start in range(size*2 + 1) ]
    return izip_longest(*phased_iterators, fillvalue='')


def words_with_context(words):
    """
    >>> words = ('cane', 'gatto', 'olio', 'corda', 'tavolo', 'orto')
    >>> words_with_context(words).next()
    ('olio', u'cane gatto olio corda tavolo')
    """
    for group in make_groups(words, 2):
        yield (group[2], ' '.join(group),)
  


def parse(text):
    return words_with_context(text.split())

def search(text, word, size):
    """
    >>> result = search('Sulle cime e sulle rape non ci sono alberi', 'ci', 2)
    >>> result.next()
    u'rape non ci sono alberi'
    """
    def contains(group):
        return group[size] == word
    from itertools import ifilter
    return ifilter(contains, make_groups(text.split(), size))

    
