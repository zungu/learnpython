#!/usr/bin/python

from sys import argv

#sets the parameters for argv, names the script and says it wants the filename
script, filename = argv

#simple test that calls the filename you defined above in the CLI
print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

#allows the user to abort with ^C or to continue with RETURN
raw_input("?")


print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#the parentheses keep it as one argument.  the \n are next to the operands to sepearte the lines.  start, newline, newline, new line, defines the lines.  or -> target.write ("\n" .join([line1,line2,line3]))

target.write("%s \n%s \n%s \n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

