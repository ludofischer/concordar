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
        self.assertEqual(self.sequence, ((0,2,'La'), (1, 8,'capra'), (2, 14,'canta')))

    def test_lowercase(self):
        extractor = concordance.lowercase_extractor('terror')
        self.assertEqual(1,extractor(1,'Terror'))
        self.assertEqual(1,extractor(1, 'terror'))
        self.assertFalse(extractor(1, 'sunday'))
        
        extractor = concordance.lowercase_extractor('Terrier')
        self.assertEqual(1, extractor(1, 'terrier'))

    def test_positions(self):
        result = concordance.positions(self.sequence, 'capra')
        self.assertEqual(result[0], (1,8))
        
    def test_word_groups(self):
        result = concordance.build_results(self.sequence, ((0,0,2),(1,1,2)))
        self.assertEqual(result.next(), (0, ((2,'La',), (8, 'capra')))) 

    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'capra', 1)
        self.assertEqual(result.next(), (8, 'La capra canta'))


    def test_symmetric_ranges(self):
        result = concordance.symmetric_ranges((0,1,2,3,4), 2, 5)
        self.assertEqual(result.next(), (0,(0,3)))
        self.assertEqual(result.next(), (1,(0,4)))
        self.assertEqual(result.next(), (2,(0,5)))
        self.assertEqual(result.next(), (3,(1,5)))
        self.assertEqual(result.next(), (4,(2,5)))
        self.assertRaises(StopIteration, result.next)


