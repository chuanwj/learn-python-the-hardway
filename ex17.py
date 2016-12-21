
from sys import argv
from os.path import exists

script = argv[0]
from_file = argv[1]
to_file = argv[2]

print "Copy form %s to %s" % (from_file, to_file)

##
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue. CTRL-C to abort."
raw_input()

out_file = open(to_file,'w+')
out_file.write(indata)

print "\r Alright, all done. ^_^"
out_file.close()
in_file.close()

##  python.exe .\ex17.py .\ex16.py ex17.txt