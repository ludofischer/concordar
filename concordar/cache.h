#ifndef CACHE_h
#define CACHE_h

#include <vector>
#include <QString>

struct Cache {
    QString text;
    QString word;
    std::vector<QString> tokens;
    std::vector<int> positions;

};

#endif
