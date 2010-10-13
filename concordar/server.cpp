#include <vector>
#include <functional>

#include <QString>
#include <QFuture>
#include <QList>
#include <QtConcurrentFilter>

#include "cache.h"
#include "server.h"
#include "importers.h"
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
void BasicConcordanceServer::tokenize(const QString& text, std::vector<concordance::Token>& tokens) {
    importers::graphical_tokenize(text, tokens);
}

void BasicConcordanceServer::concord(int radius, std::vector<concordance::Result>& result) {
    concord(_cache->word, _cache->tokens, radius, result);
}

void BasicConcordanceServer::concord(const QString& word, const std::vector<concordance::Token>& tokens, int radius, std::vector<concordance::Result>& result) {
    QFuture<concordance::Token> matching = QtConcurrent::filtered(tokens, std::bind<bool>(concordance::word_matches, std::placeholders::_1, word));
    QList<concordance::Token> matches = matching.results();

    concordance::results(tokens, matches.toStdList(), radius, result);
}
