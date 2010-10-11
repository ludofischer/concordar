#include <QString>
#include <QFile>
#include <QIODevice>
#include <QTextStream>
#include <QTextCodec>
#include "read_text.h"

namespace utilities {
QString read_text(const QString& filename) {
  QString text;

  QFile data(filename);
  if (data.open(QIODevice::ReadOnly|QIODevice::Text)) {
 
    QTextStream text_stream (&data);
    text_stream.setCodec(QTextCodec::codecForName("UTF-8"));
    text = text_stream.readAll();
  }

  data.close();

  return text;
}
}
