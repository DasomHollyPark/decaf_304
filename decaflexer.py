import ply.lex as lex


#identify the set of tokens that will be recognized by your lexcial analyzer.


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
	'ID',
	'COMMA', 'DOT',
	'INT_CONST', 'FLOAT_CONST', 'STRING_CONST',
	'EQUALS', 'SEMICOLON',
	'LEFT_PAR', 'RIGHT_PAR',
	'LEFT_BRACE', 'RIGHT_BRACE',
	'LEFT_BRACKET', 'RIGHT_BRACKET',
	'PLUS_PLUS', 'MINUS_MINUS',
	'ARITH_OP', 'BOOL_OP', 'UNARY_OP'
] + list(reserved.values())

#Regular Expression rule

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

def t_ID(t):
	r'([a-zA-Z_][a-zA-Z_]*)'
	return t

def t_COMMA(t):
	r'([,])'
	return t

def t_SEMICOLON(t):
	r'([;])'
	return t

def t_DOT(t):
	r'([.])'
	return t

def t_EQUALS(t):
	r'([=])'
	return t

def t_INT_CONST(t):
	r'([0-9]+)'
	return t

def t_FLOAT_CONST(t):
	r'(([0-9]+[.][0-9]+)|([0-9]*[.][0-9]+)|([0-9]+[.][0-9]*))'
	return t

def t_STRING_CONST(t):
	r'(["][a-zA-Z_0-9 ]*["])'
	return t

def t_LEFT_PAR(t):
	r'([(])'
	return t

def t_RIGHT_PAR(t):
	r'([)])'
	return t

def t_LEFT_BRACE(t):
	r'([{])'
	return t

def t_RIGHT_BRACE(t):
	r'([}])'
	return t

def t_LEFT_BRACKET(t):
	r'([\[])'
	return t

def t_RIGHT_BRACKET(t):
	r'([\]])'
	return t

def t_ARITH_OP(t):
	r'([+]|[-]|[*]|[/])'
	return t

def t_PLUS_PLUS(t):
	r'([+][+])'
	return t

def t_MINUS_MINUS(t):
	r'([-][-])'
	return t

def t_BOOL_OP(t):
	r'([&][&]|[|][|]|[=][=]|[!][=]|[<]|[>]|[<][=]|[>][=])'
	return t

def t_PLUS(t):
	r'[+]'
	return t

def t_MINUS(t):
	r'[-]'
	return t

def t_TIMES(t):
	r'[*]'
	return t

def t_DIVIDED_BY(t):
	r'[/]'
	return t

t_ignore  = ' \t'

lexer = lex.lex()

# Test it out
#data = "hi"

# Give the lexer some input

#lexer.input(data)

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
    #tok.lexpos is the index of the token relative to the start of the input text.
#    print(tok.type, tok.value, tok.lineno, tok.lexpos)

