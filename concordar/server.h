class BasicConcordanceServer {
 public:
  void concordance(const QString&, int, const std::vector<QString>&);
  void tokenize(const QString&, std::vector<QString>&, std::vector<int>&);
};  
