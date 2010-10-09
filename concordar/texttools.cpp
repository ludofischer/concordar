#include <QDebug>
#include <Qt>
#include <QMainWindow>
#include <QFileDialog>
#include <QDir>
#include <QString>
#include <QModelIndex>
#include <QTextCursor>
#include <QKeySequence>
#include "ui_main_window.h"
#include "texttools.h"
#include "cache.h"
#include "read_text.h"

TextTools::TextTools(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow), cache(new Cache)  {
  
  ui->setupUi(this);
  ui->actionQuit->setShortcut(QKeySequence::Quit);
  ui->actionOpen->setShortcut(QKeySequence::Open);
  connect_slots();
}

TextTools::~TextTools() {
  delete ui;
}

void TextTools::construct_layout() {
}

void TextTools::connect_slots() {
    connect(ui->actionOpen, SIGNAL(triggered()), this, SLOT(choose_file()));
    connect(ui->actionQuit, SIGNAL(triggered()), qApp, SLOT(quit()));
}

void TextTools::setup_basic_concordance() {
}

void TextTools::prepare_browser() {
}

void TextTools::highlight_selected_word(QTextCursor& cursor) {
}

void TextTools::choose_file() {
    QString filename = QFileDialog::getOpenFileName(this, tr("Choose file to study"), QDir::homePath(), tr("Text files (*.txt)"));
    QString text = utilities::read_text(filename);
    ui->textBrowser->blockSignals(true);
    ui->textBrowser->setPlainText(text);
    ui->textBrowser->blockSignals(false);
}
void TextTools::build_for_word_selected_in_text() {
}

void TextTools::build_for_typed_word(const QString& word)  {
}

void TextTools::show_occurrence_context(QModelIndex&){
}

void TextTools::update_concordance() {
}
