#ifndef SERVER_h
#define SERVER_h

#include <vector>
#include <QString>

class BasicConcordanceServer {
 public:
  void concordance(const QString&, int, const std::vector<QString>&);
  void tokenize(const QString&, std::vector<QString>&, std::vector<int>&);
};  

#endif
