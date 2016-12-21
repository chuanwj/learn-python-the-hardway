from sys import argv
script, filename = argv
txt = open(filename,'r')
print "Here's your file %r:" % filename
print txt.read()
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again,'r')
print txt_again.read()