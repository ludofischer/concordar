#include <QtGui>
#include "ui_main_window.h"

class TextTools : public QMainWindow, public Ui::Ui_MainWindow {
    Q_OBJECT;
public: 
TextTools();

protected:
void import_file(); // How?

};


TextTools::TextTools() {
  setupUi(*this);
  
  actionQuit->setShortcut(QtGui::QKeySequence::Quit);
}
