import sys
import ply.yacc as yacc

try:
	f = open(sys.argv[1])
	p = yacc.yacc(f.read())
	print p
	
except EOFError:
	print "Could not open file %s." % sys.argv[1]