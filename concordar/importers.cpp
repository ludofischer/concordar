#include <vector> 
#include <QString>
#include <QTextDocument>
#include <QTextCursor>
#include "importers.h"

namespace importers {

void graphical_tokenize(const QString& text, std::vector<QString>& tokens, std::vector<int>& positions) {
    QTextDocument doc(text);
    QTextCursor cursor = QTextCursor(&doc);
    
    cursor.select(QTextCursor::WordUnderCursor);
    tokens.push_back(cursor.selectedText());
    positions.push_back(cursor.position());
       
    while(cursor.movePosition(QTextCursor::NextWord)) {
        cursor.select(QTextCursor::WordUnderCursor);
        tokens.push_back(cursor.selectedText());
        positions.push_back(cursor.position());
    }
}

}
