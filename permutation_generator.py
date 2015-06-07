#!/usr/bin/env python3
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

class permutation_generator:
	def __init__(self, iter_generator, length):
		self.iter_generator = iter_generator
		self.length = length
		self.iterators = []
		for i in range(length):
			self.iterators.append(iter(iter_generator))
		self.next_list = []
		for it in self.iterators:
			self.next_list.append(next(it))
		self.done = False
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.done:
			raise StopIteration

		old_list = self.next_list.copy()
		for i in range(self.length):
			try:
				new_value = next(self.iterators[i])
				self.next_list[i] = new_value
				break
			except StopIteration:
				if i == self.length - 1:
					self.done = True
				self.iterators[i] = iter(self.iter_generator)
				self.next_list[i] = next(self.iterators[i])
		return old_list
