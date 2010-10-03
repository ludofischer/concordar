#include <QString>
#include <vector>

#include "read_file.h"
#include "importer.h"

int main() {
  QString text = read_text("../../samples/moby_dick.txt");
  std::vector<Token> tokens;
  tokenize(text, tokens);
  return 0;
}
