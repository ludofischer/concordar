# -*- coding: utf-8 -*-
import unittest
from PyQt4 import QtGui
from concordar import concordance

class ConcordanceTest(unittest.TestCase):
    def setUp(self):
        self.sentence = ("La capra è nell'orto")
        self.sequence = ('La', 'capra', 'è', 'nell', 'orto')

