# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import unittest2 as unittest
from PyQt4 import QtGui
from concordar import concordance

class ConcordanceTest(unittest.TestCase):
    def setUp(self):
        self.sentence = ("La capra è nell'orto")
        self.sequence = ('La', 'capra', 'è', 'nell', 'orto')

