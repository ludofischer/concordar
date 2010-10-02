# -*- coding: utf-8 -*-

from __future__ import  unicode_literals
import unittest2 as unittest
from concordar import models

class ModelsTest(unittest.TestCase):

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
        

    def test_server_concordance(self):
        server = models.BasicConcordanceServer()
        result = server.tokenize('Love is in the air')
        self.assertEqual(result, ((4, 'Love'),(7, 'is'),(10, 'in'), (14, 'the'), (18, 'air')))
        result = server.concordance( 'in', 1, result)        

        
