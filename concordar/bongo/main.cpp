#include <QString>
#include <vector>
#include <map>

#include "read_file.h"
#include "importer.h"

int main() {
  QString text = read_text("../../samples/moby_dick.txt");
  std::vector<QString> tokens;
  std::map<int, int> converter;
  tokenize(text, tokens, converter);
  return 0;
}
