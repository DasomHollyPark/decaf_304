import ply.lex as lex

#To handle reserved words, you should write a single rule 
#to match an identifier and do a special name lookup in a function
reserved = {
	'boolean' : 'BOOLEAN',
	'break' : 'BREAK',
	'continue' : 'CONTINUE',
	'class' : 'CLASS',
	'do' : 'DO',
	'else' : 'ELSE',
	'extends' : 'EXTENDS',
	'false' : 'FALSE',
	'float' : 'FLOAT',
	'for' : 'FOR',
	'if' : 'IF',
	'int' : 'INT',
	'new' : 'NEW',
	'null' : 'NULL',
	'private' : 'PRIVATE',
	'public' : 'PUBLIC',
	'return' : 'RETURN',
	'static' : 'STATIC',
	'super' : 'SUPER',
	'this' : 'THIS',
	'true' : 'TRUE',
	'void' : 'VOID',
	'while' : 'WHILE',
}

tokens = [
	'ID', 'COMMA',
	'DOT', 'NUMBER',
	'EQUALS', 'SEMICOLON',
	'STRING_CONST',
	'LEFT_PAR', 'RIGHT_PAR',
	'LEFT_BRACE', 'RIGHT_BRACE',
	'LEFT_BRACKET', 'RIGHT_BRACKET',
	'PLUS_PLUS', 'MINUS_MINUS',
	'ARITH_OP', 'BOOL_OP', 'UNARY_OP'
] + list(reserved.values())