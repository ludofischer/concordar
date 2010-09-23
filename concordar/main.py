#! /usr/bin/env python
# -*- coding: utf-8 -*-

#   copyright 2010 Ludovico Fischer

#    This file is part of Concordance.
#
#    Concordance is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Concordance is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Concordance.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
import sip
sip.setapi('QVariant', 2)
sip.setapi('QString', 2)


import sys
from PyQt4 import QtGui
from texttools import TextTools

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    text_tools = TextTools()
    text_tools.actionQuit.triggered.connect(app.quit)
    text_tools.show()
    app.exec_() 
