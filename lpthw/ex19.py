#!/usr/bin/python

def cheese_and_crackers(cheese_count, boxes_of_crackers): 
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "\nWe can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math and variables inside too:"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 10)

print "Or just math:"
cheese_and_crackers(10 + 20, 30 + 30)

