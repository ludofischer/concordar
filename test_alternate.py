from __future__ import unicode_literals
import unittest2
from concordar import alternate


class AlternateTest(unittest2.TestCase):
    def test_import(self):
        text = 'La capra canta'
        result = alternate.import_file(text)
        self.assertEqual(result, ('La', 'capra', 'canta'))
