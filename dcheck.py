#!/usr/bin/python
# a simple calculator with die rolls. good tool during games.
#
# Copyright (C) 2015 - Blake Lowe
#
# This file is part of rpg-utils.
#
# rpg-utils is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# rpg-utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rpg-utils. If not, see <http://www.gnu.org/licenses/>.
#
import random
from collections import deque
import readline
from enum import Enum

class token:
	# all operators are left-associative
	precedence_values = {'d': 4,  '*': 3,  '/': 3,  '+': 2, '-': 2, 'v': 1}
	
	class type(Enum):
		operator = 1
		number = 2
		paren = 3
	
	def __init__(self, value, type):
		self.value = value
		self.type = type

	def precedence(self):
		return token.precedence_values[self.value]

def dresolve(num,  sides):
	print("Rolling ",  num,  "d",  sides,  ":",  sep = '')
	rolls = []
	for i in range(0,  num):
		rolls.append(random.randint(1,  sides))
	print("\tRolls:",  rolls)
	total = sum(rolls)
	print("\tTotal:",  total)
	print()
	return total
	
def vresolve(roll1,  roll2):
	print("Contesting Rolls:")
	print("\tPlayer 1's Roll:",  roll1)
	print("\tPlayer 2's Roll:",  roll2)
	if roll1 > roll2:
		print("Player 1 Wins!")
	elif roll1 == roll2:
		print("It's a tie!")
	else:
		print("Player 2 Wins!")
	print()
	return roll1 - roll2
	
opstack = deque() # used to keep operators and parens while parsing
postfix = deque() # holds the fully-parsed query
def parse(new_token): # parses a new token into postfix
	if new_token.type == token.type.number:
		# numbers are ready to go on the stack
		postfix.append(new_token)
	elif new_token.type == token.type.operator:
		# at this point, we need to hold this operator on our
		# temporary opstack. however, any operators with
		# higher precedence on the top of opstack are ready
		# to be moved to postfix
		while len(opstack) > 0 and \
		opstack[-1].type == token.type.operator and \
		new_token.precedence() <= opstack[-1].precedence():
			postfix.append(opstack.pop())
		opstack.append(new_token)
	elif new_token.type == token.type.paren:
		if new_token.value == '(':
			opstack.append(new_token)
		elif new_token.value == ')':
			# everything on opstack between the top and
			# the last open paren can be moved to postfix
			while len(opstack) > 0 and \
			opstack[-1].value != '(':
				postfix.append(opstack.pop())
			if len(opstack) == 0:
				print("parser error: mismatched parens")
			opstack.pop() # throw away used open paren

user_input = input("Enter roll: ")
while user_input != "exit":
	getting_number = False # kept True while a full number is being scanned
	number = 0 # temporary value to hold number while it is being scanned
	vcount = 0 # counts number of 'v's obtained --- illegal to be more than 1
	for c in user_input:
		if c >= '0' and c <= '9': # is (part of) a number
			number *= 10
			number += int(c)
			getting_number = True
		elif c in token.precedence_values: # is an operator
			if getting_number:
				parse(token(number, token.type.number))
				number = 0
				getting_number = False
			if c == 'v':
				vcount += 1
			parse(token(c, token.type.operator))
		elif c == '(' or c == ')': # is a paren
			if getting_number:
				parse(token(number, token.type.number))
				number = 0
				getting_number = False
			parse(token(c, token.type.paren))
		# unrecognized characters (inlcuding whitespace) are skipped
	# we have reached the end of our input, so clean up any temporaries
	if getting_number:
		parse(token(number, token.type.number))
		number = 0
		getting_number = False
	while len(opstack) > 0:
		last_token = opstack.pop()
		if last_token.type == token.type.paren:
			print("parser error: mismatched parens")
		postfix.append(last_token)

	print("Postfix: ", end = '')
	for tk in postfix:
		print(tk.value, end = ' ')
	print()
	print()

	# now that we have our query in nice postfix, we begin resolution
	if vcount > 1:
		print("resolution error: v used more than once")
	else:
		if vcount == 1:
			print("Resolving Opposed Check:")

		stack = deque() # only holds ints, used for calculation
		for tk in postfix:
			if tk.type == token.type.number:
				stack.append(tk.value)
			elif tk.type == token.type.operator:
				if tk.value == 'd': # die roll
					num_sides = stack.pop()
					num_dice = stack.pop()
					stack.append(dresolve( \
							num_dice, num_sides))
				elif tk.value == 'v':
					p2roll = stack.pop()
					p1roll = stack.pop()
					stack.append(vresolve(p1roll, p2roll))
				elif tk.value == '*':
					m2 = stack.pop()
					m1 = stack.pop()
					stack.append(m1 * m2)
				elif tk.value == '/':
					d2 = stack.pop()
					d1 = stack.pop()
					stack.append(d1 // d2)
				elif tk.value == '+':
					a2 = stack.pop()
					a1 = stack.pop()
					stack.append(a1 + a2)
				elif tk.value == '-':
					s2 = stack.pop()
					s1 = stack.pop()
					stack.append(s1 - s2)
		if len(stack) != 1:
			print("resolution error: malformed command")
			print("dumping contents of stack:")
			for n in reversed(stack):
				print(n)
			print()
		else:
			if vcount == 0:
				print("Final Result:", stack.pop())
				print()

	postfix = deque()
	opstack = deque()
	user_input = input("Enter roll: ")
