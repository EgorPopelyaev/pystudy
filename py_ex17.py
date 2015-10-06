from sys import argv
from os.path import exists

script, source, dest = argv

def copyFromFile(from_file, to_file):
	print "Copy from %r file to %r" % (from_file, to_file)
	in_data = open(from_file).read()
	exists(to_file)
	print "Ready, hit RETURN to continue, CTRK-C to abort."
	raw_input()
	open(to_file, 'w').write(in_data)
	print "Done!"

copyFromFile(source, dest)