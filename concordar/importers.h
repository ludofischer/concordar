#ifndef IMPORTERS_h
#define IMPORTERS_h

#include <vector> 
#include <QString>
#include <QTextDocument>
#include <QTextCursor>
#include "concordance.h"

namespace importers {
    void graphical_tokenize(const QString&, std::vector<concordance::Token>&);
}

#endif
