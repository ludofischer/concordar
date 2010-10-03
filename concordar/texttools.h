#ifndef TEXT_TOOLS_h
#define TEXT_TOOLS_h

#include <QMainWindow>
#include <QString>
#include <QTextCursor>
#include <QModelIndex>
#include "ui_main_window.h"

class TextTools : public QWidget {
  
  Q_OBJECT

  public:
  TextTools(QWidget *parent = 0);
  ~TextTools();
                                    
public slots:
  void update_concordance();
  
                                              
private slots:
  void choose_file();
  void build_for_word_selected_in_text();
  void build_for_typed_word(const QString&);
  void show_occurrence_context(QModelIndex&);

private:
  Ui::MainWindow *ui;
  void construct_layout();
  void connect_slots();
  void setup_basic_concordance();
  void prepare_browser();
  void highlight_selected_word(QTextCursor&);
                           
};

#endif
