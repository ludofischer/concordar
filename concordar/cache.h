class Cache {
 public:
    void change_working_file(const QString&);
private:
  QString word;
  std::vector<QString> tokens;
  std::vector<int> positions;
};
