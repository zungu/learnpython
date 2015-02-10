#!/usr/bin/python


#define a variable string that calls the number 10
x = "There are %d types of people." % 10

#defines the variable binary
binary = "binary"
#defines the variable do_not
do_not = "don't"

#defines the variable y, and calls the operands binary and do not
y = "Those who know %s and those %s." % (binary, do_not)

#prints the variable x, defined above
print x

#prints the variable y, defined above
print y

#prints a string, calling a variable x defined above
print "I said: %r." % x

#prints a string, calling a variable y defined above
print "I also said: '%s'." % y

#set variable hilarious as false
hilarious = False

#sets variable joke_evaluation as a string, calling a defined operand %r, which is defined above as the variable x.  X also calls another operand %10
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the variable joke_evaluation, which calls, r, r is defined as false
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#adds the strings above together. 
print w + e
