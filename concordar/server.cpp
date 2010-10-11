#include <vector>
#include <QString>

#include "cache.h"
#include "server.h"
#include "importers.h"

BasicConcordanceServer::BasicConcordanceServer() {}

void BasicConcordanceServer::set_cache(Cache *cache) {
    _cache = cache;
}

void BasicConcordanceServer::tokenize() {
    if (_cache->tokens.empty()) {
        tokenize(_cache->text, _cache->tokens, _cache->positions);
    }
}
void BasicConcordanceServer::tokenize(const QString& text, std::vector<QString>& tokens, std::vector<int>& positions) {
    importers::graphical_tokenize(text, tokens, positions);
}

void BasicConcordanceServer::concordance(const QString& word, const std::vector<QString>& tokens, int radius, std::vector<QString>& result) {
}
