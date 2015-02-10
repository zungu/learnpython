from sys import exit
from random import randint

class Game(object):

	def __init__(self, start):
		self.lost = [
		  "Too drunk, go home",
		  "You can't handle it, leave sucka",
		  "Taxi for one!",
		  "Pole Sana Rafiki",
		  ]
		self.start = start

	def play(self):
		next = self.start

		while True:
			print "\n---------------------------"
			room = getattr(self, next)
			next = room()

	def death(self):
		print self.lost[randint(0, len(self.lost)-1)]
		exit(1)

	def home(self):
		print """You're sitting at home on a Friday night, bored.   Do you want to go out?"""

		action = raw_input("> ")

		if action == "Yes" or action == "yes":
			print """Excellent, lets get started on the DSM bar crawl!"""
			return('qbar')
		else:
			print "Sorry, let me rephrase that..."
			return('home')

	def qbar(self):
		print """Congratulations on making it to the first bar on your journey tonight.  Each bar will present challenges that you must pass 
		in order to move onto the next bar.  You get a great prize at the end of this, so lets go."""
		print """Upon entering Qbar, you see several groups, the Rugby Boys, the regulars, and the tourists.  Which group do you go hang out with?"""

		action = raw_input("> ")

		if action == "Rugby Boys":
			print """These guys are pretty fratty..."""
			return('rugby_boys')
		elif action == "regulars":
			print """The regulars are smoking cigarrettes and hanging out with the whores."""
			return('regulars')
		elif action == "tourists":
			return('tourists')
		else: 
			print	 "You're not cool enough to hang out by yourself, or anyone else..."
			return('qbar')

	def rugby_boys(self):
		print """ Now you're hanging with the boys!  Alright, jager bombs.  How many do you want?"""

		jager_bomb = raw_input("> ")
		amount = "%d" % 3 

		while jager_bomb != amount:
			print "Try again..."
			jager_bomb = raw_input("> ")

		if amount == jager_bomb:
			print """That's right, 3 for the best, lets carry on now."""
			return('lukas')

	def regulars(self):
		print """The regulars huh?  This is going to get interesting... Just as you begin to sit down, a huge whore walks over to you and sticks her
		hand down your pants.  You look at her horrified, realizing this is exactly how you get AIDS.  What do you do?"""

		action = raw_input("> ")

		if action == "run away":
			print """Sorry that's just the way you spread it..."""
			return('death')
		elif action == "pour alcohol on it":
			print """Quick thinking, you saved yourself!..."""
			return('lukas')
		else:
			print"""You still have a chance, try 'run away' or 'pour water on it'"""
			return('regulars')

	def tourists(self):
		print """These tourists can't dance, it's a mess on the dance floor, chaos really.  So what do you do?"""

		action = raw_input("> ")

		if action == "dance":
			print"""That's the way to be, they invite you into their circle and start grinding on you."""
			return('lukas')
		else: 
			print"""There is only one answer- 'dance'"""
			return('tourists')




a_game = Game('home')
a_game.play()

