#include "cache.h"

void Cache::set_text(const QString& text) {
    _text = text;
}
    
QString Cache::get_text() const {
    return _text;
}
