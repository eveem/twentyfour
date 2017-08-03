import random
import itertools

def can_twentyfour ():
	print ':',
	alllist = list (itertools.permutations (arr))
	for l in alllist:
		print l
	return True

command = "WELCOME TO TWENTY-FOUR GAMES"

while (command != "exit"):
	arr = []
	for i in xrange (4):
		num = random.randrange (1, 9)
		arr.append (num)
	print arr,
	if can_twentyfour ():
		print '/',
	else:
		print 'X',

	command = raw_input ()