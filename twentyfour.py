import random

command = "HI"

while (command != "exit"):
	for i in xrange (4):
		print random.randrange (1, 9),
	command = raw_input ()