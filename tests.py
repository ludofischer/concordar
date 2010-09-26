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
        self.assertEqual(result.next(), (0,(0,3)))
        self.assertEqual(result.next(), (1,(0,4)))
        self.assertEqual(result.next(), (2,(0,5)))
        self.assertEqual(result.next(), (3,(1,5)))
        self.assertEqual(result.next(), (4,(2,5)))
        self.assertRaises(StopIteration, result.next)

    def test_get_word_groups(self):
        result = concordance.get_word_groups(self.sequence, ((0, (0,2)), (2,(1,4))))
        result_slice = result.next()
        result_tuple = (result_slice[0], tuple(result_slice[1]))
        self.assertEqual(result_tuple, (0, ('La', 'capra')))


    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'è', 1)
        self.assertEqual(result.next(), (2,'capra è nell'))
        self.assertRaises(StopIteration, result.next)

from concordar import models

class ModelsTest(unittest.TestCase):
    def test_text_model(self):
        model = models.TextModel('La capra è nel bosco')
        self.assertEqual(model.rowCount(), 5)
        self.assertEqual(model.data(model.index(0,0)), 'La')
        self.assertEqual(model.data(model.index(2,0)), 'è')

    def test_concordance_model(self):
        model = models.ConcordanceModel(((2,'La capra è'), (5, 'una capra bruca',)))
        self.assertEqual(model.rowCount(), 2)
        self.assertEqual(model.columnCount(), 2)
        model_index = model.index(0, 1)
        self.assertEqual('La capra è', model.data(model_index))
        model_index = model.index(1, 1)
        self.assertEqual('una capra bruca', model.data(model_index))

        model.set_matches(((1, 'il tonno è'), (34, 'la velocità dei galli')))
        model_index = model.index(0, 1)
        self.assertEqual('il tonno è', model.data(model_index))

