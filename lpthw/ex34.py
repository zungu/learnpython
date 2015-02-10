#!/usr/bin/python

from sys import exit

def runway_club():
	print "You have arrived at Runway."
	print "This place is going to be either wild and wonderful, or the end of you."
	print "I wish you luck in your quest."
	print "To start, do you buy a girl a drink, or yourself a drink?"
	
	next = raw_input("> ")
	
	if next == "girl":
		return "you got laid, congratulations!"
	elif 