import random
import itertools

op = ['+', '-', '*', '/']

def can_twentyfour ():
	print ':',
	all_num = gen_permute_number ()
	all_opt = gen_op ()
	return True

def gen_permute_number ():
	return list (itertools.permutations (arr))

def gen_op ():
	all_op = []
	for i in op:
		for j in op:
			for k in op:
				temp = []
				temp.append (i)
				temp.append (j)
				temp.append (k)
				all_op.append (temp)
	return all_op

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