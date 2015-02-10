#!/usr/bin/python

from sys import argv

script, input_file = argv

#defines the function, the j can be any letter
def print_all(j):
	print j.read()
	
def rewind (j) : 
	j.seek(0)

# defines a function, with a variable inside of it.  line_count is a variable cleverly named so that the user knows what it is doing.  later on, on line 31, we establish the current line.
def print_a_line(line_count, j) :
	print line_count, j.readline()
	
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind (current_file)

print "Let's print three lines:\n"

#establishes the current line as line #1 in the .txt file
current_line = 1
#calls up to def print_a_line and counts the above current line to read it
print_a_line(current_line, current_file)

#adds one more line to current line, so now it is reading the second line
current_line = current_line + 1

#calls up to def print_a_line and counts +1 to readline(2) now
print_a_line(current_line, current_file)

#adds one more line to current_line, which is 2 from above.  So now 3
current_line = current_line + 1

#reads line 3 of the .txt file that is current_file
print_a_line(current_line, current_file)

