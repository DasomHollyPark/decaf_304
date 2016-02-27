import sys
import ply.lex as lex
from decaflexer import tokens
import ply.yacc as yacc

#########################################################
###################<FIELD DECLARATION>###################
#########################################################



def p_start(p):
	'''start : method_decl
	         | constructor_decl
	         | field_decl
	         | literal
	         | field_access'''
	pass

def p_field_decl(p):
	'''field_decl : modifier var_decl'''
	

def p_modifier(p):
	'''modifier : 
       modifier : PUBLIC
       modifier : PUBLIC STATIC
       modifier : PRIVATE
       modifier : PRIVATE STATIC
       modifier : STATIC
	'''

	
#var_decl ::= type variables;
def p_var_decl(p):
	'var_decl : type variables SEMICOLON'
	

# type ::= int | float | boolean 
def p_type(p):
	"""type : INT
			| FLOAT 
			| BOOLEAN""" 
	p[0] = p[1]

###variables ::= variable (, variable)*###
#Variables -> variable variable2
def p_variables(p):
	'variables : variable variable2'
	p[0] = p[1]

#variable2 -> E | , variable variable2
def p_variable2(p):
	'''variable2 : 
	   variable2 : COMMA variable variable2'''

# variable ::= id
def p_variable(p):
	'variable : ID'
	p[0] = p[1]


############################################################################
###################<METHODS AND CONSTRUCTORS DECLARATION>###################
############################################################################

#method_decl ::= modifier (type | void) id (formals?) block

def p_method_decl(p) :
	'''method_decl : modifier type ID 
	   method_decl : modifier type ID formals
	   method_decl : modifier VOID ID 
	   method_decl : modifier VOID ID formals
	'''

#constructor_decl ::= modifier id (formals) block
def p_constructor_decl(p):
	'''constructor_decl : modifier ID
	   constructor_decl : modifier ID formals'''



#formals ::= formal_param (, formal_param)*
def p_formals(p):
	'formals : formal_param formal_param2'
	

def p_formal_param2(p):
	'''formal_param2 : 
	   formal_param2 : COMMA formal_param formal_param2'''

#formal_param ::= type variable
def p_formal_param(p):
	'formal_param : type variable'


###################################################
###################<EXPRESSIONS>###################
###################################################


def p_literal(p):
	'''literal : STRING_CONST 
			   | NULL
		       | TRUE
		       | FALSE'''

def p_primary(p):
	'''primary : literal
			   | THIS
			   | SUPER'''

def p_field_access(p):
	'''field_access : primary DOT ID
					| ID
	'''	

def p_error(p):
#    print("Syntax error in input")
    print("Syntax error at '%s'" % repr(p))


parser = yacc.yacc()


while True:
   try:
       s = raw_input('> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
