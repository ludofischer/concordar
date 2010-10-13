#ifndef IMPORTERS_h
#define IMPORTERS_h

#include <vector> 
#include <QString>
#include <QTextDocument>
#include <QTextCursor>
#include "token.h"

namespace importers {
    void graphical_tokenize(const QString&, std::vector<Token>&);
}

#endif
