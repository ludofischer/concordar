#include <QWidget>

namespace Ui {
}
class TextTools : public QWidget {
  
  Q_OBJECT

  public:
  TextTools(QWidget *parent = 0);
  void change_working_file(filename);
                                    
public slots:
  void move_cursor_to_word(const QModelIndex&);
  void update_concordance();
                           
                                              
private slots:
  void choose_file();
  void new_word_selected_in_text();
  void new_word_typed(const Qstring&);
  
private:
  QString Word;
};
