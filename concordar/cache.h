#ifndef CACHE_h
#define CACHE_h

#include <vector>
#include <QString>
#include "concordance.h"

struct Cache {
    QString text;
    QString word;
    std::vector<concordance::Token> tokens;

};

#endif
