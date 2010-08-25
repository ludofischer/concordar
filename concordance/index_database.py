# -*- coding: utf-8 -*-

#    copyright 2010 Ludovico Fischer

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
#


from __future__ import unicode_literals
import sys
from PyQt4.QtSql import *

"""
This has to be updated to use a QSqlTableModel, to be able to pass it to a QListView'
"""

def create_database():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')
    if not db.open():
        print 'Database error: {1}'.format(db.lastError().text())
        sys.exit(1)
    return db

def create_table(db):
        query = QSqlQuery(db)
        query.exec_('CREATE TABLE words_locations(word TEXT, context TEXT, book_name TEXT)')

def insert_word(db, pairs, book_name='default'):
    db.transaction()
    query = QSqlQuery(db)
    query.prepare('INSERT INTO words_locations (word, context, book_name) VALUES (?, ?, ?)')

    for word, context in pairs:
        query.addBindValue(word)
        query.addBindValue(context)
        query.addBindValue(book_name)
        
        query.exec_()
    db.commit()

def retrieve_contexts(db, word):
    query = QSqlQuery(db)
    query.prepare('SELECT context, book_name FROM words_locations WHERE word = ?')
    
    query.addBindValue(word)
    
    query.exec_()
    
    while query.next():
        yield query.value(0)
    
