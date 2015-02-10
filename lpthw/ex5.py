#!/usr/bin/python

my_name = 'Jon C. Gore'
my_age = 25 #getting old
my_height = 74 # inches
my_weight = 185 # lbs
my_eyes = 'Hazel'
my_teeth = 'White'
my_hair = 'Brown'

cm_in_inch = 2.54
pounds_in_kilo = 2.25


print "Let's talk about %s." % my_name
print "He's %d inches tall, which is %d centimeters tall." % (my_height, cm_in_inch * my_height)
print "He's %d pounds heavy, or %d kilograms heavy." % (my_weight, my_weight / pounds_in_kilo )
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it right

print "If I add %d, %d, and %d I get %d. " % (my_age, my_height, my_weight, my_age + my_height + my_weight)
