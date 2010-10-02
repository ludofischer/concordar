from __future__ import unicode_literals
import sip
sip.setapi('QVariant', 2)
sip.setapi('QString', 2)

import unittest2
from concordar import concordance, importers


class AlternateTest(unittest2.TestCase):
    def setUp(self):
        self.text = 'La capra canta'
        self.sequence = importers.import_file(self.text)

    def test_import(self):
        self.assertEqual(self.sequence, ((2,'La'), (8,'capra'), (14,'canta')))

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

   
    def test_positions(self):
        result = concordance.positions(self.sequence, 'capra')
        self.assertEqual(result.next(), (1,8))
        
    def test_word_groups(self):
        result = concordance.get_word_groups(self.sequence, ((0,0,2),(1,1,2)))
        self.assertEqual(result.next(), (0, ((2,'La',), (8, 'capra')))) 

    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'capra', 1)
        self.assertEqual(result.next(), (8, 'La capra canta'))


