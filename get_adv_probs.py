#!/usr/bin/env python3
# Quick calculator for probabilities of rolls with
# advantage/disadvantage -- where a d20 is rolled twice and
# the highest or lowest score is selected.
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

def higher(roll1, roll2):
	if roll1 > roll2:
		return roll1
	else:
		return roll2

def lower(roll1, roll2):
	if roll1 < roll2:
		return roll1
	else:
		return roll2

adv_roll_counts = {}
disadv_roll_counts = {}
for i in range(0, 20):
	adv_roll_counts[i+1] = 0
	disadv_roll_counts[i+1] = 0

for i in range(0, 20):
	for j in range(0, 20):
		adv_roll_counts[higher(i+1, j+1)] += 1
		disadv_roll_counts[lower(i+1, j+1)] += 1

print("Advantage Probabilities:\t|\tDisadvantage Probabilities:")
for i in range(0, 20):
	print("Probability of\t", i+1, ": ", \
	      round(adv_roll_counts[i+1] / 20**2 * 100, 2), \
	      "%\t|\tProbability of\t", i+1, ": ", \
	      round(disadv_roll_counts[i+1] / 20**2 * 100, 2), "%", sep = '')
