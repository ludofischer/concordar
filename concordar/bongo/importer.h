#ifndef IMPORTER_h
#define IMMPORTER_h

#include <vector>
#include <QString>

typedef struct {
  QString token;
  int coordinate;
  int index;
} Token;

void tokenize(const QString&, std::vector<Token>&);

#endif
