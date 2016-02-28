import sys
import ply.lex as lex
from decaflexer import tokens
import ply.yacc as yacc

########################################################
################### EMPTY STRING #######################
########################################################

def p_empty(p):
	'''
		empty : 
	'''

########################################################
#################### START STATE #######################
########################################################

def p_start(p):
	'''
		start : class_decl_star
	'''

########################################################
#################### CLASS DECL ########################
########################################################

def p_class_decl_star(p):
	'''
		class_decl_star : empty
		class_decl_star : class_decl class_decl_star
	'''

def p_class_decl(p):
	'''
		class_decl : CLASS ID extends LEFT_BRACE class_body_decl_plus RIGHT_BRACE
	'''

def p_extends_opt(p):
	'''
		extends_opt : empty
		extends_opt : extends
	'''

def p_extends(p):
	'''
		extends : EXTENDS ID
	'''

def p_class_body_decl_plus(p):
	'''
		class_body_decl_plus : class_body_decl class_body_decl_plus
		class_body_decl_plus : class_body_decl
	'''

def p_class_body_decl(p):
	'''
		class_body_decl : field_decl
		class_body_decl : method_decl
		class_body_decl : constructor_decl
	'''

########################################################
###################### FIELDS ##########################
########################################################

def p_field_decl(p):
	'''
		field_decl : modifier var_decl
	'''

def p_modifier(p):
	'''
		modifier : empty
		modifier : PUBLIC
		modifier : PRIVATE
		modifier : PUBLIC STATIC
		modifier : PRIVATE STATIC
		modifier : STATIC
	'''

def p_var_decl(p):
	'''
		var_decl : type variables SEMICOLON
	'''

def p_type(p):
	'''
		type : INT
		type : FLOAT
		type : BOOLEAN
		type : ID
	'''

def p_variables(p):
	'''
		variables : variable more_variables
	'''

def p_more_variables(p):
	'''
		more_variables : empty
									 | COMMA variable more_variables
	'''

def p_variable(p):
	'''
		variable : ID array_dim_star
	'''

def p_array_dim_star(p):
	'''
		array_dim_star : empty
		array_dim_star : array_dim array_dim_star
	'''

def p_array_dim(p):
	'''
		array_dim : LEFT_BRACKET RIGHT_BRACKET
	'''

########################################################
##################### METHODS ##########################
########################################################

def p_method_decl(p):
	'''
		method_decl : modifier type_or_void ID LEFT_PAR formals_opt RIGHT_PAR block
	'''

def p_type_or_void(p):
	'''
		type_or_void : type
		type_or_void : VOID
	'''

def p_constructor_decl(p):
	'''
		constructor_decl : modifier ID LEFT_PAR formals_opt RIGHT_PAR block
	'''

def p_formals_opt(p):
	'''
		formals_opt : empty
		formals_opt : formals
	'''

def p_formals(p):
	'''
		formals : formal_param more_formals
	'''

def p_more_formals(p):
	'''
		more_formals : empty
		more_formals : COMMA formal_param more_formals
	'''

def p_formal_param(p):
	'''
		formal_param : type variable
	'''

########################################################
#################### STATEMENTS ########################
########################################################

def p_block(p):
	'''
		block : LEFT_BRACE stmt_star RIGHT_BRACE
	'''

def p_stmt_star(p):
	'''
		stmt_star : empty
		stmt_star : stmt stmt_star
	'''

def p_stmt(p):
	'''
		stmt : IF LEFT_PAR expr RIGHT_PAR stmt else_opt
		stmt : WHILE LEFT_PAR expr RIGHT_PAR stmt
		stmt : FOR LEFT_PAR stmt_expr_opt SEMICOLON expr_opt SEMICOLON stmt_expr_opt RIGHT_PAR stmt
		stmt : RETURN expr_opt SEMICOLON
		stmt : stmt_expr SEMICOLON
		stmt : BREAK SEMICOLON
		stmt : CONTINUE SEMICOLON
		stmt : block
		stmt : var_decl
		stmt : SEMICOLON
	'''

def p_else_opt(p):
	'''
		else_opt : empty
		else_opt : ELSE stmt
	'''

########################################################
################### EXPRESSIONS ########################
########################################################

def p_literal(p):
	'''
		literal : INT_CONST
		literal : FLOAT_CONST
		literal : STRING_CONST
		literal : NULL
		literal : TRUE
		literal : FALSE
	'''

def p_primary(p):
	'''
		primary : literal
		primary : THIS
		primary : SUPER
		primary : LEFT_PAR expr RIGHT_PAR
		primary : NEW ID LEFT_PAR arguments_opt RIGHT_PAR
		primary : lhs
		primary : method_invocation
	'''

def p_arguments_opt(p):
	'''
		arguments_opt : empty
		arguments_opt : arguments
	'''

def p_arguments(p):
	'''
		arguments : expr more_expr
	'''

def p_more_expr(p):
	'''
		more_expr : empty
		more_expr : COMMA expr more_expr
	'''

def p_lhs(p):
	'''
		lhs : field_access
		lhs : array_access
	'''

def p_field_access(p):
	'''
		field_access : primary DOT ID
		field_access : ID
	'''

def p_array_access(p):
	'''
		array_access : primary LEFT_BRACKET expr RIGHT_BRACKET
	'''

def p_method_invocation(p):
	'''
		method_invocation : field_access LEFT_PAR arguments_opt RIGHT_PAR
	'''

def p_expr(p):
	'''
		expr : primary
		expr : assign
		expr : new_array
		expr : expr ARITH_OP expr
		expr : expr BOOL_OP expr
		expr : UNARY_OP expr
	'''

def p_assign(p):
	'''
		assign : lhs EQUALS expr
		assign : lhs PLUS_PLUS
		assign : PLUS_PLUS lhs
		assign : lhs MINUS_MINUS
		assign : MINUS_MINUS lhs
	'''

def p_new_array(p):
	'''
		new_array : NEW type array_expr_plus
	'''

def p_array_expr_plus(p):
	'''
		array_expr_plus : array_expr array_expr_plus
		array_expr_plus : array_expr
	'''

def p_array_expr(p):
	'''
		array_expr : LEFT_BRACKET expr RIGHT_BRACKET
	'''

def p_array_empty_star(p):
	'''
		array_empty_star : empty
		array_empty_star : array_empty array_empty_star
	'''

def p_array_empty(p):
	'''
		array_empty : LEFT_BRACKET RIGHT_BRACKET
	'''

def p_stmt_expr(p):
	'''
		stmt_expr : assign
		stmt_expr : method_invocation
	'''

########################################################
###################### PARSER ##########################
########################################################

parser = yacc.yacc()

while True:
   try:
       s = raw_input('> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
