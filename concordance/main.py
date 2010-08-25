# -*- coding: utf-8 -*-

import sip
sip.setapi('QVariant', 2)
sip.setapi('QString', 2)

import sys
from PyQt4 import QtGui
from texttools import TextTools

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    text_tools = TextTools()
    text_tools.show()
    app.exec_() 
