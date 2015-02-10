#usr/bin/python

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#sets up a while loop, that reads the length of the variable stuff, while the length is less than 10.
while len(stuff) != 10:
  #create a function, named next_one which pops items from more_stuff to next_one.
  next_one = more_stuff.pop()
  #prints "adding" and the remaining items in next_one which will be popped
  print "Adding: ", next_one
  
  #appends to stuff the new items in next_one
  stuff.append(next_one)
  print "There's %d items now." %len(stuff)
  
print "There we go: ", stuff
  
print "Let's do some things with stuff."

print stuff[1]
print stuff[:1]
print stuff.pop()
#join(' ', things)
print ' '.join(stuff)
# join('#', stuff[3:5])
print '#'.join(stuff[3:5])
print more_stuff
  