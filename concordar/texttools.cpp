#include <QWidget>
#include <QString>
#include <QModelIndex>
#include <QTextCursor>
#include <QKeySequence>
#include "ui_main_window.h"
#include "texttools.h"

TextTools::TextTools(QWidget *parent) : QWidget(parent), ui(new Ui::MainWindow)  {
  
  ui->setupUi(this);
  ui->actionQuit->setShortcut(QKeySequence::Quit);
}

TextTools::~TextTools() {
  delete ui;
}

void TextTools::construct_layout() {
}

void TextTools::connect_slots() {
}

void TextTools::setup_basic_concordance() {
}

void TextTools::prepare_browser() {
}

void TextTools::highlight_selected_word(QTextCursor& cursor) {
}

void TextTools::choose_file() {
}
void TextTools::build_for_word_selected_in_text() {
}

void TextTools::build_for_typed_word(const QString& word)  {
}

void TextTools::show_occurrence_context(QModelIndex&){
}
