import sys
import ply.yacc as yacc
from decafparser import *

argv = sys.argv
argc = len(argv)

if argc < 2:
	print "Missing input file as command line argument."
	sys.exit(1)

try:
	f = open(sys.argv[1])
	p = yacc.yacc()
	result = p.parse(f.read())
	f.close()
	print result
	
except EOFError:
	print "Could not open file %s." % sys.argv[1]