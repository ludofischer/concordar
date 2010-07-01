from PyQt4.QtSql import QSqlTableModel

concordanceModel =  QSqlTableModel()
concordanceModel.setTable('words_locations')
concordanceModel.select()
