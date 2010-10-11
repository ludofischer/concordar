#include "server.h"

BasicConcordanceServer::BasicConcordanceServer() {}

void BasicConcordanceServer::set_cache(Cache *cache) {
    _cache = cache;
}

void BasicConcordanceServer::tokenize(const QString& text, std::vector<QString>& tokens, std::vector<int>& positions) {
}

void BasicConcordanceServer::concordance(const QString& word, const std::vector<QString>& tokens, int radius, std::vector<QString>& result) {
}
