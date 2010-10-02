#include <QString>
#include <QFile>
#include <QIODevice>
#include <QTextStream>

QString read_text(const QString& filename) {
  QString text;

  QFile data(filename);
  if (data.open(QIODevice::ReadOnly)) {
 
    QTextStream text_stream (&data);
    text = text_stream.readAll();
  }

  data.close();

  return text;
}
