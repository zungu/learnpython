#!/usr/bin/python

from sys import argv

#defines two items to be inputted for argv

(script, user_name) = argv
prompt1 = 'give me an answer you ass > '
prompt2 = 'I\'ll murder ye grandmotha if ye don\'t tell me > '
prompt3 = 'Sorry please answer, I\'m just having a bad day > '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#defines a new variable, likes, with what the user enters into raw_input.  
likes = raw_input(prompt1)

print "Where do you live %s?" % user_name
#defines a new variable "lives" with a user generated input
lives = raw_input(prompt2)

print "What kind of computer do you have?"
#defines a new variable, "computer" with a user generated input.
computer = raw_input(prompt3)

print """
Ok, so you said %r about liking me.
You live in %r.  That is a cool place.
And you have a %r computer.  Sweet!
""" % (likes, lives, computer) #calls the variables the user entered