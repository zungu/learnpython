#This is a string of items
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#prints the text below
print "Wait there's not 10 things in that list, let's fix that."

#creates a variable that points to ten_things and then splits the string every place there is a space
stuff = ten_things.split(' ')
#creates a list of 8 different words
more_stuff = ["Day,", "Night", "Song", "frisbee", "corn", "Banana", "Girl", "Boy"]

#Function that scans the amount of words in stuff split by a space, and if the amount is less than ten will run the code below.
while len(stuff) !=10:
	#creates a variable named next_one, which scanes more_stuff and pops off the last item in the more_stuff list.
	next_one = more_stuff.pop()
	#prints "adding" and the last itemt that was popped off of the more_stuff list.
	print "Adding: ", next_one
	#adds the last item to be popped off to the stuff list.
	stuff.append(next_one)
	#prints the amount of items in stuff
	print "There's %d items now." % len(stuff)

#prints the final list of stuff after there are 10 items in the list
print "There we go: ", stuff

print "Let's do some things with stuff."

#prints the first item in the list
print stuff[1]
#prints the first item the list from the right hand side
print stuff[-1]
#prints the last item on stuff as a new item popped off
print stuff.pop()
#prints stuff list with a - between each of the items
print '-'.join(stuff)
print '#'.join(stuff[3:5])

