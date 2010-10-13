#ifndef SERVER_h
#define SERVER_h

#include <vector>
#include <QString>
#include "cache.h"
#include "concordance.h"

class BasicConcordanceServer {
 public:
    BasicConcordanceServer();
    void concord(const QString&, const std::vector<concordance::Token>&, int, std::vector<concordance::Result>&);
    void concord(int, std::vector<concordance::Result>&);
    void tokenize(const QString&, std::vector<concordance::Token>&);
    void tokenize();
    void set_cache(Cache*);
private:
    Cache *_cache;
};  

#endif
