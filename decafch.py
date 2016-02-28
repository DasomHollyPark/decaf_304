import sys
import ply.yacc as yacc
from decafparser import *

argv = sys.argv
argc = len(argv)

if argc < 2:
	print "Missing input file as command line argument."
	sys.exit(1)

try:
	f = open(argv[1])
	parser = yacc.yacc()
	result = parser.parse(f.read())
	f.close()

	if result != None:
		print result
	
except EOFError:
	print "Could not open file %s." % argv[1]