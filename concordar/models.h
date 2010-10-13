#ifndef MODELS_h
#define MODELS_h

#include <vector>
#include <QAbstractTableModel>
#include <QModelIndex>
#include <QVariant>

#include "concordance.h"

class ConcordanceModel : public QAbstractTableModel {
public:
    int columnCount(const QModelIndex&) const;
    int rowCount(const QModelIndex&) const ;
    QVariant data(const QModelIndex&, int) const;
    void set_results(const std::vector<concordance::Result>&);
private:
    std::vector<concordance::Result> results;
};

#endif
