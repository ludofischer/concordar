#include <vector>
#include <functional>

#include <QString>
#include <QFuture>
#include <QtConcurrentFilter>

#include "cache.h"
#include "server.h"
#include "importers.h"
#include "token.h"
#include "concordance.h"

BasicConcordanceServer::BasicConcordanceServer() {}

void BasicConcordanceServer::set_cache(Cache *cache) {
    _cache = cache;
}

void BasicConcordanceServer::tokenize() {
    if (_cache->tokens.empty()) {
        tokenize(_cache->text, _cache->tokens);
    }
}
void BasicConcordanceServer::tokenize(const QString& text, std::vector<Token>& tokens) {
    importers::graphical_tokenize(text, tokens);
}

void BasicConcordanceServer::concordance(const QString& word, const std::vector<Token>& tokens, int radius, std::vector<QString>& result) {
    QFuture<Token> matching = QtConcurrent::filtered(tokens, std::bind<bool>(concordance::word_matches, std::placeholders::_1, word));
}
