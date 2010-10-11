#ifndef SERVER_h
#define SERVER_h

#include <vector>
#include <QString>
#include "cache.h"

class BasicConcordanceServer {
 public:
    BasicConcordanceServer();
    void concordance(const QString&, const std::vector<QString>&, int, std::vector<QString>&);
    void tokenize(const QString&, std::vector<QString>&, std::vector<int>&);
    void tokenize();
    void set_cache(Cache*);
private:
    Cache *_cache;
};  

#endif
