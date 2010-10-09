#ifndef SERVER_h
#define SERVER_h

#include <vector>
#include <QString>
#include "cache.h"

class BasicConcordanceServer {
 public:
    BasicConcordanceServer();
    void concordance(const QString&, int, const std::vector<QString>&);
    void tokenize(const QString&, std::vector<QString>&, std::vector<int>&);
    
private:

};  

#endif
