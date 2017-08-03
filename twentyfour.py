import random
import itertools

operator = ['+', '-', '*', '/']

def can_twentyfour ():
	print ':',
	all_num = gen_permute_number ()
	all_opt = gen_op ()
	for nm in all_num:
		for ot in all_opt:
			equation = merging (nm, ot)
			# print equation
	return True

def gen_permute_number ():
	return list (itertools.permutations (arr))

def gen_op ():
	op = []
	for i in operator:
		for j in operator:
			for k in operator:
				temp = []
				temp.append (i)
				temp.append (j)
				temp.append (k)
				op.append (temp)
	return op

def merging (num, opt):
	temp = []
	p = 0
	for i in xrange (7):
		if i % 2 == 0:
			temp.append (num[p])
		else:
			temp.append (opt[p])
			p += 1
	return temp

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