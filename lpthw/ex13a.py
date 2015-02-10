#!/usr/bin/python

from sys import argv

script, yes, true, maybe = argv

print "You are working on:", script
print "This script is magical, it will tell you if your crush's favorite things match yours." 

print "What is your favorite color? ", raw_input(), yes
print "Do you want to get married in the next three years? ", raw_input(), true
print "Is sex important to you? ", raw_input(), maybe


