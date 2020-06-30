#include <lexer-core/lexer.h>

#include <iostream>

int main()
{
	Lexer lexer;
	
	if(lexer.isEqual("Hello", "World!"))
	{
		std::cout<<"EQUAL!";
	}
	else
	{
		std::cout<<"NOT EQUAL!";
	}
	
	return 0;
}
