#!/usr/bin/python

#this piece of code is like the argv in scripts

def print_two(*args): 
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#that *args is actually pointless, it is easier to do this

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2) 

# this takes one argument 

def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments 

def print_none():
	print "I got nothin'."
	

print_two("Jon", "Gore")
print_two_again("Is", "awesome")
print_one("FOREAL")
print_none()