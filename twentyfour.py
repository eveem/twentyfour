import math
import random
import itertools

operator = ['+', '-', '*', '/']

def add_bk (eq):
	temp = []
	temp.append (eq)
	temp.append ('(' + eq[:7] + ')' + eq[7:])
	temp.append (eq[:4] + '(' + eq[4:11] + ')' + eq[11:])
	temp.append (eq[:8] + '(' + eq[8:] + ')')
	temp.append ('(' + eq[:11] + ')' + eq[11:])
	temp.append (eq[:4] + '(' + eq[4:] + ')')
	temp.append ('(' + eq[:7] + ')' + eq[7] + '(' + eq[8:] + ')')
	return temp

def can_twentyfour ():
	print ':',
	all_num = gen_permute_number ()
	all_opt = gen_op ()
	for nm in all_num:
		for ot in all_opt:
			equation = merging (nm, ot)
			all_eq = add_bk (equation)
			for eq in all_eq:
				try:
					result = eval (eq)
				except ZeroDivisionError:
					result = 0
				
				if result == 24.00:
					print eq
					return True
	return False

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
	eq = ''.join (temp)	
	return eq

command = "WELCOME TO TWENTY-FOUR GAMES"

while (command != "exit"):
	arr = []
	for i in xrange (4):
		tmp = random.uniform (1, 9)
		num = str (math.ceil(tmp))
		arr.append (num)
	# arr.append ('7.0')
	# arr.append ('5.0')
	# arr.append ('3.0')
	# arr.append ('3.0')
	print arr,
	
	raw_input ()
	if can_twentyfour ():
		print '/'
	else:
		print 'X'