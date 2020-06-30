#include <lexer-core/lexer.h>

Lexer::Lexer(QObject* parent) 
	: QObject(parent)
{

}

Lexer::~Lexer()
{

}

bool Lexer::isEqual(const QString& a, const QString& b) const
{
	return 0  == QString::compare(a, b, Qt::CaseInsensitive);
}
