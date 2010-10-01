from __future__ import unicode_literals
import sip
sip.setapi('QVariant', 2)
sip.setapi('QString', 2)

import unittest2
from concordar import concordance


class AlternateTest(unittest2.TestCase):
    def setUp(self):
        self.text = 'La capra canta'
        self.sequence = concordance.import_file(self.text)

    def test_import(self):
        result = concordance.import_file(self.text)
        self.assertEqual(result, ((2,'La'), (8,'capra'), (14,'canta')))
   
    def test_positions(self):
        result = concordance.positions(self.sequence, 'capra')
        self.assertEqual(result.next(), (1,8))
        
    def test_word_groups(self):
        result = concordance.get_word_groups(self.sequence, ((0,0,2),(1,1,2)))
        self.assertEqual(result.next(), (0, ((2,'La',), (8, 'capra')))) 

    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'capra', 1)
        self.assertEqual(result.next(), (8, 'La capra canta'))


