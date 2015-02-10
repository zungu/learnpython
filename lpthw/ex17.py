#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#Calls the from_file and to_file that we defined above in the CLI
print "Copying from %s to %s" % (from_file, to_file)

#How do you put these on one line.
input = open(from_file)
#creates a variable that reads the above variable
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input( ">")

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

