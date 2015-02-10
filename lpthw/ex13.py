#!/usr/bin/python

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Set's up a variable that allows the user to type something along with argv.  argv will come up in the CLI as calling the above statement. script, first, second, third. 

this_is_confusing = raw_input(argv)

print this_is_confusing + "These are my answers." 
