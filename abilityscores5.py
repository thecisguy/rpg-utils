#!/usr/bin/env python3
# ability score generator for DnD 5th ed.
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

def get_score():
	roll = []
	min = 7
	removed = False
	for num in range(0,  4):
		newroll = random.randint(1,  6)
		if newroll < min:
			min = newroll
		roll.append(newroll)
	print("Rolls: ",  roll)
	
	highestthree = []	
	for num in range(0,  4):
		if roll[num] == min and not removed:
			removed = True
		else:
			highestthree.append(roll[num])
	print("Highest Three: ",  highestthree)
	
	total = sum(highestthree)
	print("Final Score:",  total)
	return total
	
print("Rolling Dice:")
all_scores = []
for num in range(0,  6):
	print("Score ",  num + 1,  ":", sep = '')
	score = get_score()
	print()
	all_scores.append(score)

all_scores.sort()
all_scores.reverse()
print("Final Scores: ",  all_scores)
