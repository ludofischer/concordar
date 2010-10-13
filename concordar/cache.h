#ifndef CACHE_h
#define CACHE_h

#include <vector>
#include <QString>
#include "token.h"

struct Cache {
    QString text;
    QString word;
    std::vector<Token> tokens;

};

#endif
