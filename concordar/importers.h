#ifndef IMPORTERS_h
#define IMPORTERS_h

#include <vector> 
#include <QString>
#include <QTextDocument>
#include <QTextCursor>

namespace importers {
void graphical_tokenize(const QString&, std::vector<QString>&, std::vector<int>&);
}

#endif
