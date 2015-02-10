#Else and if:
#If statements create 'branchs' in the code.  It tells the code "if this statement is true, run the code, otherwise skip it"	

people = 1
cars = 41
buses = 40

#print output if cars are more than people
if cars > people and buses == people:
	print "We should take the cars."
#print statement below if true	
elif cars < people and people == buses:
	print "We should not take the cars"
#if neither of two statements are true, print statement below
else:
	print "We can't decide."

#print statement if true
if buses > cars:
	print "That's too many buses."
#print statement if true
elif buses < cars:
	print "Maybe we could take the buses."
#if neither of two above statements are true, print the below
else:
	print "we still can't decide."

#final statement, print output
if people > buses:
	print "Alright, let's just take the buses"
#if above statement is not true, print below
else:
	print "Fine, let's stay home then."

