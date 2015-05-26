#!/usr/bin/env python3
# Small test program to determine the average ability score obtained through
# the random ability score generation option in D&D 5th ed.
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

def get_score(roll):
	min = 7
	for r in roll:
		if r < min:
			min = r

	removed = False
	highestthree = []	
	for num in range(0,  4):
		if roll[num] == min and not removed:
			removed = True
		else:
			highestthree.append(roll[num])
	
	total = sum(highestthree)
	return total
	
total_scores = 0
for i in range(0, 6):
	for j in range(0, 6):
		for k in range(0, 6):
			for l in range(0, 6):
				cur_rolls = [i+1, j+1, k+1, l+1]
				print("Rolls:", cur_rolls, end = '')
				nscore = get_score(cur_rolls)
				total_scores += nscore
				print(", Score:", nscore)
print("Average =", total_scores, "/", 6**4, "=", total_scores / 6**4)
