#include <vector>
#include <QTextDocument>
#include <QTextCursor>
#include <QString>


void tokenize(const QString& text, std::vector<QString>& tokens, std::vector<int>& index_coord) {
  QTextDocument *doc = new QTextDocument(text);
  QTextCursor cursor(doc);

  cursor.select(QTextCursor::WordUnderCursor);
  tokens.push_back(cursor.selectedText());
  index_coord.push_back(cursor.position());

  while (cursor.movePosition(QTextCursor::NextWord)) {
    cursor.select(QTextCursor::WordUnderCursor);
    tokens.push_back(cursor.selectedText());
    index_coord.push_back(cursor.position());

  }
  delete doc;
}
