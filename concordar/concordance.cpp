#include <list>
#include <vector>

#include <QDebug>
#include "concordance.h"

namespace concordance {

bool word_matches(const Token& token, const QString& word) {
    return token.word.toLower() == word.toLower();}

    
    std::list<size_t> ranges(size_t number, size_t radius, size_t max) {
        size_t start;
        size_t end;
        if (number < radius ) {
            start = 0;
        } else {
            start = number - radius;
        }
        
        if (number + radius > max) {
            end = max;
        } else {
            end = number + radius;
        }
        
        std::list<size_t> result;
        result.push_back(start);
        
        while (start != end) {
            ++start;
            result.push_back(start);
        }
        return result;
    }

    void results(const std::vector<Token>& all, const std::list<Token>& matching, size_t radius, std::vector<Result>& results) {
        qDebug() << "entered concordance.";
        qDebug() << matching.size();
        for (std::list<Token>::const_iterator it = matching.begin(); it != matching.end(); ++it) {
            Result result;
            std::list<size_t> contexts = ranges(it->index, radius, all.size());

            for (std::list<size_t>::const_iterator it = contexts.begin(); it != contexts.end(); ++it) {
                size_t index = *it;
                QString word = all[index].word;
                qDebug() << word;
                result.sentence << word;
            }

            result.position = it->position;
            results.push_back(result);
        }
    }
}

