#!/usr/bin/python
# ability score generator for DnD 5th ed.
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
