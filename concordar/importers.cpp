#include <vector> 
#include <QString>
#include <QTextDocument>
#include <QTextCursor>
#include "importers.h"
#include "token.h"

namespace importers {

    void graphical_tokenize(const QString& text, std::vector<Token>& tokens) {
    QTextDocument doc(text);
    QTextCursor cursor = QTextCursor(&doc);
    
    int index = 0;
    cursor.select(QTextCursor::WordUnderCursor);

    Token token;
    token.index = index;
    token.word= cursor.selectedText();
    token.position = cursor.position();
    tokens.push_back(token);

    while(cursor.movePosition(QTextCursor::NextWord)) {
        Token token;
        ++index;
        cursor.select(QTextCursor::WordUnderCursor);
        token.index = index;
        token.word= cursor.selectedText();
        token.position = cursor.position();
        tokens.push_back(token);
      
    }
}

}
