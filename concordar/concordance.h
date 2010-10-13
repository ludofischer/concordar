#ifndef CONCORDANCE_h
#define CONCORDANCE_h

#include <list>
#include <vector>
#include <QString>
#include <QStringList>

namespace concordance {
    


    struct Token {
        QString word;
        int index;
        int position;
    };

    struct Result {
        int position;
        QStringList sentence;
    };

    bool word_matches(const Token&, const QString&);
    
    std::list<size_t> ranges(size_t, size_t, size_t);
    void results(const std::vector<Token>& all, const std::list<Token>& matching, size_t radius, std::vector<Result>& results);
}

#endif
