
import sys
from PyQt4.QtSql import *

"""
This has to be updated to use a QSqlTableModel, to be able to pass it to a QListView'
"""
class DatabaseConnection(object):
    pass

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

def insert_word(db, word, context, book_name):
    query = QSqlQuery(db)
    query.prepare('INSERT INTO words_locations (word, context, book_name) VALUES (?, ?, ?)')
    
    query.addBindValue(word)
    query.addBindValue(context)
    query.addBindValue(book_name)

    query.exec_()

def retrieve_contexts(db, word):
    query = QSqlQuery(db)
    query.prepare('SELECT context, book_name FROM words_locations WHERE word = ?')
    
    query.addBindValue(word)
    
    query.exec_()
    
    result_set = []

    while query.next():
        pass
    
