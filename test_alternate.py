import unittest
from concordar import concordance, importers


class AlternateTest(unittest.TestCase):
    def setUp(self):
        self.text = 'La capra canta'
        self.sequence = importers.graphical_tokenize(self.text)

    def test_import(self):
        self.assertEqual(self.sequence, ((0,2,'La'), (1, 8,'capra'), (2, 14,'canta')))

    def test_lowercase(self):
        extractor = concordance.lowercase_extractor('terror')
        self.assertTrue(1,extractor('Terror'))
        self.assertTrue(1,extractor('terror'))
        self.assertFalse(extractor('sunday'))
        
        extractor = concordance.lowercase_extractor('Terrier')
        self.assertTrue(extractor('terrier'))

    def test_positions(self):
        result = concordance.matching_indices(self.sequence, 'capra')
        self.assertEqual(next(result), 1)
        
    def test_build_results(self):
        result = concordance.build_results(self.sequence, ((0,0,2),(1,1,2)))
        self.assertEqual(next(result), (2,'La capra',)) 

    def test_all(self):
        result = concordance.search_sequence(self.sequence, 'capra', 1)
        self.assertEqual(next(result), (8, 'La capra canta'))


    def test_symmetric_ranges(self):
        result = concordance.symmetric_ranges((0,1,2,3,4), 2, 5)
        self.assertEqual(next(result), (0,0,3))
        self.assertEqual(next(result), (1,0,4))
        self.assertEqual(next(result), (2,0,5))
        self.assertEqual(next(result), (3,1,5))
        self.assertEqual(next(result), (4,2,5))
        self.assertRaises(StopIteration, next, result)


if __name__ == '__main__':
    unittest.main()
