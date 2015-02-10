print "You enter Qbar on a hot saturday night.  Do you approach the pool table or the bar?"

decision1 = raw_input("> ")

if decision1 =="pool table":
	print "You come across Anders, the mighty Swede.  What do you do?"
	print "1. Challenge him to game of pool."
	print "2. Buy him a drink."

	anders = raw_input("> ")

	if anders == "1":
		print "Anders destroys you in pool and your spirits are crushed, leaving you equivilant to a puddle of jello"
	elif anders == "2":
		print "Anders accepts your beer, and promptly orders a bunga bunga party for you.  Do you accept?"
	else:
		print "You're an idiot, pick a right answer or the swede will destroy you."

	bunga = raw_input("> ")

	if bunga =="yes":
		print "First rule of bunga bungas is you do not speak of bunga bungas.  Well done."
	if bunga == "no":
		print "You just made a horrible mistake.  Go back to being normal."


elif decision1 == "bar":
	print "Welcome to the best Bar in Dar es Salaam."
	print "1. Drink a beer"
	print "2. Drink Konyagi"
	print "3. Drink the drink offered to you by a beautiful young lady."

	drinks = raw_input("> ")

	if drinks == "1" or drinks =="2":
		print "Excellent choice, time for some pool now."
		print anders
	else:
		print "You wake up the next morning with no money, no phone, and an STD."
else:
	print "You are mauled by a bodyguard and break a neck.  Good job!"