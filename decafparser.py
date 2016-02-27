import sys
import ply.lex as lex
from decaflexer import tokens
import ply.yacc as yacc

#########################################################
###################<FIELD DECLARATION>###################
#########################################################


#Start States
def p_start(p):
	'''start : field_decl
					 | constructor_decl
	         | method_decl
	         | literal
	         | field_access'''

# field_decl ::= modifier var_decl
def p_field_decl(p):
	'''field_decl : modifier var_decl'''
	
#modifier ::= (public | private)? (static)?
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
			| BOOLEAN
			| ID"""

###variables ::= variable (, variable)*###

#Variables -> variable variable2
def p_variables(p):
	'variables : variable variable2'

#variable2 -> E | , variable variable2
def p_variable2(p):
	'''variable2 : 
	   variable2 : COMMA variable variable2'''

# variable ::= id
def p_variable(p):
	'variable : ID'

############################################################################
###################<METHODS AND CONSTRUCTORS DECLARATION>###################
############################################################################

#method_decl ::= modifier (type | void) id (formals?) block
def p_method_decl(p) :
	'''method_decl : modifier type ID LEFT_PAR RIGHT_PAR block
	   method_decl : modifier type ID LEFT_PAR formals RIGHT_PAR block
	   method_decl : modifier VOID ID LEFT_PAR RIGHT_PAR block
	   method_decl : modifier VOID ID LEFT_PAR formals RIGHT_PAR block
	'''

def p_block(p):
	'''
		block : LEFT_BRACE stmts RIGHT_BRACE
	'''

def p_stmts(p):
	'''
		stmts : stmt stmt2
	'''

def p_stmt(p):
	'''
		stmt : SEMICOLON
	'''

def p_stmt2(p):
	'''
		stmt2 : stmts
		stmt2 : 
	'''

#constructor_decl ::= modifier id (formals) block
def p_constructor_decl(p):
	'''constructor_decl : modifier ID LEFT_PAR RIGHT_PAR
	   constructor_decl : modifier ID LEFT_PAR formals RIGHT_PAR'''

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

#literal ::= float_const | string_const | null | true | false
def p_literal(p):
	'''literal : STRING_CONST 
			   | NULL
		       | TRUE
		       | FALSE'''

#primary ::= literal | this | super | (expr) | new id (arguments?) | lhs | method_invocation
def p_primary(p):
	'''primary : literal
			   | THIS
			   | SUPER'''

#lhs ::= field_access 
def p_lhs(p):
	'lhs : field_access'

#field_access ::= primary.ID | ID
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
