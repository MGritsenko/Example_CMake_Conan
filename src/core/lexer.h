#include<lexer-core/exports.h>

#include<QtCore>
#include<QString>

class LEXER_CORE_EXPORT Lexer : public QObject
{
public:
	Lexer(QObject* parent = 0);
	~Lexer();
	
	bool isEqual(const QString& a, const QString& b) const;
};
