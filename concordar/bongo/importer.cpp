#include <vector>
#include <QTextDocument>
#include <QTextCursor>
#include <QString>
#include "importer.h"

void tokenize(const QString& text, std::vector<Token>& tokens) {
  QTextDocument *doc = new QTextDocument(text);
  QTextCursor cursor(doc);
  int index = 0;

  cursor.select(QTextCursor::WordUnderCursor);
  Token token;
  token.token = cursor.selectedText();
  token.coordinate = cursor.position();
  token.index = index;
  ++index;
  tokens.push_back(token);
  while (cursor.movePosition(QTextCursor::NextWord)) {
    
    cursor.select(QTextCursor::WordUnderCursor);
    Token token;
    token.token = cursor.selectedText();
    token.coordinate = cursor.position();
    token.index = index;
    ++index;
    tokens.push_back(token);
  }
  delete doc;
}
