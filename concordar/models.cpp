#include <vector>
#include <Qt>
#include <QAbstractTableModel>
#include <QModelIndex>
#include <QVariant>

#include "concordance.h"
#include "models.h"

int ConcordanceModel::columnCount(const QModelIndex& parent = QModelIndex()) const {
    return 2;
}

int ConcordanceModel::rowCount(const QModelIndex& parent = QModelIndex()) const {
    if (parent.isValid() ) {
        return 0;
    } else {
        return static_cast<int>(results.size());
    }
}

QVariant ConcordanceModel::data(const QModelIndex& index, int role = Qt::DisplayRole) const {
    if (!index.isValid()) {
        return QVariant();
    }
    
    if (role == Qt::DisplayRole) {
        return results[index.row()].sentence.join(" ");
    } else {
        return QVariant();
    }
}

void ConcordanceModel::set_results(const std::vector<concordance::Result>& things) {
    beginResetModel();
    results = things;
    endResetModel();
}
