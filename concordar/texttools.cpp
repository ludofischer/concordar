#include <QDebug>
#include <Qt>
#include <QWidget>
#include <QMainWindow>
#include <QFileDialog>
#include <QDir>
#include <QString>
#include <QModelIndex>
#include <QTextCursor>
#include <QTextEdit>
#include <QBrush>
#include <QColor>
#include <QMessageBox>
#include <QKeySequence>
#include "ui_main_window.h"
#include "texttools.h"
#include "cache.h"
#include "server.h"
#include "read_text.h"

TextTools::TextTools(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow), cache(new Cache), server(new BasicConcordanceServer)  {
    construct_layout();
    connect_slots();
}

TextTools::~TextTools() {
  delete ui;
  delete cache;
}

void TextTools::construct_layout() {
    ui->setupUi(this);
    ui->actionQuit->setShortcut(QKeySequence::Quit);
    ui->actionOpen->setShortcut(QKeySequence::Open);
    
    QWidget *viewport = ui->textBrowser->viewport();
    viewport->setCursor(Qt::PointingHandCursor);
    ui->radiusBox->setMinimum(1);
}

void TextTools::connect_slots() {
    connect(ui->actionOpen, SIGNAL(triggered()), this, SLOT(choose_file()));
    connect(ui->actionQuit, SIGNAL(triggered()), qApp, SLOT(quit()));
    connect(ui->actionAbout, SIGNAL(triggered()), this, SLOT(about_info()));

    connect(ui->textBrowser, SIGNAL(cursorPositionChanged()), this, SLOT(build_for_word_selected_in_text()));
    connect(ui->radiusBox, SIGNAL(valueChanged(int)), this, SLOT(update_concordance()));
}

void TextTools::setup_basic_concordance() {
    ui->textBrowser->blockSignals(true);
    ui->textBrowser->setPlainText(cache->text);
    ui->textBrowser->blockSignals(false);
    server->set_cache(cache);
    server->tokenize();
}

void TextTools::highlight_selected_word(QTextCursor& cursor) {
    QTextEdit::ExtraSelection selection;
    selection.format.setBackground(QBrush(QColor("yellow")));
    selection.cursor = cursor;
    QList<QTextEdit::ExtraSelection> extraSelections;
    extraSelections.append(selection);
    ui->textBrowser->setExtraSelections(extraSelections);
}

void TextTools::choose_file() {
    QString filename = QFileDialog::getOpenFileName(this, tr("Choose file to study"), QDir::homePath(), tr("Text files (*.txt)"));
    if (!filename.isEmpty()) {
        import_file(filename);
        setup_basic_concordance();
    } 
}

void TextTools::import_file(const QString& filename) {
    QString text = utilities::read_text(filename);
    cache->text = text;
}
 

void TextTools::build_for_word_selected_in_text() {
    QTextCursor cursor = ui->textBrowser->textCursor();
    cursor.select(QTextCursor::WordUnderCursor);
    highlight_selected_word(cursor);
    QString word = cursor.selectedText();
    cache->word = word;
    ui->searchBox->setText(word);
    update_concordance();
}

void TextTools::build_for_typed_word(const QString& word)  {
    cache->word = word;
    update_concordance();
}

void TextTools::show_occurrence_context(QModelIndex&){
}

void TextTools::update_concordance() {

}

void TextTools::about_info() {
    QMessageBox msgBox;
    msgBox.setWindowTitle("Concordar");
    msgBox.setText("Concordar");
    msgBox.setInformativeText(tr("Copyright 2010 Ludovico Fischer"));
    msgBox.setDefaultButton(QMessageBox::Ok);
    msgBox.exec();
}
