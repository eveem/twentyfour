import random

def can_twentyfour ():
	print ':',
	return True

command = "WELCOME TO TWENTY-FOUR GAMES"

while (command != "exit"):
	for i in xrange (4):
		print random.randrange (1, 9),
	if can_twentyfour ():
		print '/',
	else:
		print 'X',
	command = raw_input ()