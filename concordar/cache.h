#ifndef CACHE_h
#define CACHE_h

#include <vector>
#include <QString>

class Cache {
 public:
    Cache() {}
    void change_working_file(const QString&);
    std::vector<QString> get_tokens();
    void set_tokens(const std::vector<QString>& the_tokens) { tokens = the_tokens; }
    void set_positions(const std::vector<int>& the_positions) {
        positions = the_positions; }
    void set_word(QString& word) { _word = word; }
    QString word() const { return _word; }
    void set_text(const QString&);
    QString get_text() const;
private:
  QString _word;
  QString _text;
  std::vector<QString> tokens;
  std::vector<int> positions;
};

#endif
