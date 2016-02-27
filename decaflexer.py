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
	'ID', 'COMMA',
	'DOT', 'NUMBER',
	'EQUALS', 'SEMICOLON',
	'STRING_CONST',
	'LEFT_PAR', 'RIGHT_PAR',
	'ARITH_OP', 'BOOL_OP',
	'UNARY_OP', 'LEFT_BRACE',
	'RIGHT_BRACE'
] + list(reserved.values())

#Regular Expression rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_COMMA(t):
	r'[,]'
	t.type = reserved.get(t.value, 'COMMA')
	return t

def t_SEMICOLON(t):
	r'[;]'
	t.type = reserved.get(t.value, 'SEMICOLON')
	return t

def t_NUMBER(t):
	r'[+||-]*[0-9][0-9]*'
	t.type = reserved.get(t.value, 'NUMBER')
	return t

def t_DOT(t):
	r'[.]'
	t.type = reserved.get(t.value, 'DOT')
	return t

def t_EQUALS(t):
  	r'[\=]'
  	return t

def t_STRING_CONST(t):
  	r'["][a-zA-Z_0-9 ][a-zA-Z_0-9 ]*["]'
	return t

def t_LEFT_PAR(t):
	r'[(]'
	return t

def t_RIGHT_PAR(t):
	r'[)]'
	return t

def t_LEFT_BRACE(t):
	r'[{]'
	return t

def t_RIGHT_BRACE(t):
	r'[}]'
	return t

def t_ARITH_OP(t):
	r'[+||-||*||/]'
	return t

def t_BOOL_OP(t):
	r'[&&||||||==||!=||<||>||<=||>=]'
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

