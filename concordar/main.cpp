#include <QApplication>
#include "texttools.h"

int main(int argc, char **argv) {
  QApplication app(argc, argv);
  TextTools main_window;
  main_window.show();
  return app.exec();

}
