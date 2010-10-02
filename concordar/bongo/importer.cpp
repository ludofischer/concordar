#include <map>
#include <vector>
#include <QTextDocument>
#include <QTextCursor>
#include <QString>


void tokenize(const QString& text, std::vector<QString>& tokens, std::map<int, int>& index_coord) {
  QTextDocument *doc = new QTextDocument(text);
  QTextCursor cursor(doc);
  int index = 0;

  cursor.select(QTextCursor::WordUnderCursor);
  tokens.push_back(cursor.selectedText());
  index_coord.insert(std::pair<int, int>(index, cursor.position()));
  ++index;

  while (cursor.movePosition(QTextCursor::NextWord)) {
    cursor.select(QTextCursor::WordUnderCursor);
    tokens.push_back(cursor.selectedText());
    index_coord.insert(std::pair<int, int>(index, cursor.position()));
    ++index;
  }
  delete doc;
}
