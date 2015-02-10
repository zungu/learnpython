from sys import exit

def gold_room():
	print "This room is full of gold.  How much do you take?"

	next = int(raw_input("> "))
	max = 1000
	if next < max:
		dead("congratulations, you aren't greedy. you win.")
	elif next > max:
		dead("You greedy S.O.B")
		exit(0)
	else:
		dead("Learn how to type a number.")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews your leg off.")
		elif next =="open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print why, "good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "there is a door to your right and left"
	print "which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	if next == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")

start()