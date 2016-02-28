To use the decaf syntax checker, run decafch.py with
the file you want to analyze as a command line argument:

	python decafch.py sample.decaf

The syntax checker will output any errors it finds.
If there are no errors, then there will be no output.

The parser contains shift/reduce conflicts.  However,
the checker has been sufficiently tested and these
conflicts are resolved in a way that is agreeable.