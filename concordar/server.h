#ifndef SERVER_h
#define SERVER_h

#include <vector>
#include <QString>
#include "cache.h"
#include "token.h"

class BasicConcordanceServer {
 public:
    BasicConcordanceServer();
    void concordance(const QString&, const std::vector<Token>&, int, std::vector<QString>&);
    void tokenize(const QString&, std::vector<Token>&);
    void tokenize();
    void set_cache(Cache*);
private:
    Cache *_cache;
};  

#endif
