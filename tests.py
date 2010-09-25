# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest2 as unittest

from concordar import concordance

class ConcordanceTest(unittest.TestCase):
    def setUp(self):
        self.sentence = ("La capra è nell'orto")
        self.sequence = ('La', 'capra', 'è', 'nell', 'orto')

    def test_lowercase(self):
        extractor = concordance.lowercase_extractor('terror')
        self.assertTrue(extractor('Terror'))
        self.assertTrue(extractor('terror'))
        self.assertFalse(extractor('sunday'))
        
        extractor = concordance.lowercase_extractor('Terrier')
        self.assertTrue(extractor('terrier'))

    def test_numerize(self):
        result = concordance.numerize(('dog', 'cat', 'fern'))
        self.assertEqual(result.next(), (0, 'dog'))
        self.assertEqual(result.next(), (1, 'cat'))
        self.assertEqual(result.next(), (2, 'fern'))


    def test_build_list(self):
        result = concordance.build_list(self.sentence)
        self.assertEqual(result, self.sequence)

    def test_find_positions(self):
        result = concordance.positions(self.sequence, 'orto')
        self.assertEqual(result.next(), 4)

    def test_build_ranges(self):
        result = concordance.build_ranges((0,1,2,3,4), 2, 5)
        self.assertEqual(result.next(), (0,3))
        self.assertEqual(result.next(), (0,4))
        self.assertEqual(result.next(), (0,5))
        self.assertEqual(result.next(), (1,5))
        self.assertEqual(result.next(), (2,5))
        self.assertRaises(StopIteration, result.next)

    def test_get_word_groups(self):
        result = concordance.get_word_groups(self.sequence, ((0,2), (1,4)))
        self.assertEqual(tuple(result.next()), ('La', 'capra'))
        self.assertEqual(tuple(result.next()), ('capra', 'è', 'nell'))

    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'è', 1)
        self.assertEqual(result.next(), 'capra è nell')
        self.assertRaises(StopIteration, result.next)
