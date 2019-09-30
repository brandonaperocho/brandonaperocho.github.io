# Brandon Aperocho
# Some practice to de-rust and learn from leetcode.com

""" 
Given a list, find 2 numbers that sum to t; return the numbers 
"""
	
def two_sum(num_list, t):
	"""
	:type num_list: List[int]
	:type t: int
	:rtype: [int, int]
	"""
	hash_table = {}
	for i in range (len(num_list)):
		# Check if complement exists in hashtable
		complement = t - num_list[i]
		if complement in hash_table:
			return [ complement , num_list[i] ]

		# Insert into hashtable
		d[num_list[i]] = 0
	return [0, 0]

""" 
Given 2 linked lists where the numbers are in reversed order, add the 2
	numbers with each other and return a single linked list
	Example: 
	L1: 2 -> 2 -> 2
	L2: 5 -> 8 -> 3
	return: 7 -> 0 -> 6
	since 222 + 385 = 607 
"""

class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

def two_nums_LL (L1, L2):
	"""
	:type L1: Node
	:type L2: Node
	:rtype: Node
	"""
	carry = 0
	p, q = L1, L2
	output = Node(0)
	output_tail = output

	while p or q or carry:
		# Get the values from the LL
		val1 = (p.val if p else 0)
		val2 = (q.val if q else 0)

		# Get the carry value and summed number (IE val1 + val2 + carry mod 10)
		carry, output_val = divmod(val1 + val2 + carry, 10)

		# Create next node to output LL
		output_tail.next = Node(output_val)
		output_tail = output_tail.next

		# Get next values
		p, q = p.next, q.next

	return output.next

""" 
Given an integer, reverse it. If 2 ** 31 - 1 > output > -2 ** 31 return it
	otherwise return 0
	Example: 123 -> 321
			 -120 -> -21 
"""

def reverse_int(x):
	"""
	:type x: int
	:rtype: str
	"""
	output = x
	if output % 10 == 0:
		output = int(str(x)[:-1])
	
	if output > 0:
		output = str(output)[::-1]
	else:
		output = "-" + str(-1 * output)[::-1]

	output = int(output)
	if output > ((2 ** 31) - 1) or output < -(2 ** 31):
		return 0
	else:
		return output

""" 
Given an unsorted integer array, find the smallest missing positive integer 
	Example: [0, 2, 1] -> 3
			 [3, 4, 1, -1] -> 2
	Solve in O(n) time and O(1) space 
"""

# First attempt O(n) time, O(n) space
# Idea, Insert all elements into hashtable; O(n)
# Then go through the list and count if everything is "in-place"
# Return 1 if everything is in place, otherwise return the next smallest value
def first_missing_pos (l):
	"""
	:type l: List[int]
	:rtype: int
	"""
	smallest_val = float("inf")
	hashtable = {}
	result = 1

	for i in range (len(l)):
		if l[i] < smallest_val and l[i] >= 1:
			smallest_val = l[i]

		if l[i] not in hashtable:
			hashtable[l[i]] = 0

	for i in range (len(l)):
		if (smallest_val + i) not in hashtable and (smallest_val + i) >= 1:
			result = smallest_val + i

	return result

"""
Given an array of strings, return the longest common prefix; return "" if DNE
	Example: ["abcd", "abcfg", "abd"] -> "ab"
"""
def LCP(l):
	"""
	:type l: List[str]
	:rtype str
	"""
	if len(l) == 0: return ""
	if len(l) == 1: return l[0]

	l.sort()
	str_index = 0
	for i in range (len(l[0])):
		for j in range(1, len(l)):
			if l[0][i] != l[j][i]:
				return l[0][0:str_index];
		str_index += 1
	return l[0][0:str_index]

"""
Given an array of non negative integers, find the largest container that 
can hold the most water. The container is constructed by the x and y axis. 
The bottom and top ofthe container is measured by the distance from 1 
integer to the next integer, the height is the smallest number of the 2 sides.
Example:
y
				#
	#-----------#
	#			#
	#	#		#
#	#---#---#---#	#	x	
"""

# Simple single pass, 2 pointer solution
# Start from each end and increment/decrement depending on the smallest side
# Change area once old area is smaller than new area
def max_area(l):
	"""
	:type l: List[int]
	:rtype: int
	"""
	p1, p2 = 0, len(l) - 1
	area = 0

	while (p1 < p2):
		area = max(area, abs(p1 - p2) * min(l[p1], l[p2]))

		if (l[p1] < l[p2]):
			p1 += 1
		else:
			p2 -= 1

	return area

"""
Given a string of numbers, each digital being 2-9, return all possible
letter combinations that are mapped to each number.
"""
def letter_combinations(s):
	"""
	:type s: str
	:rtype: List[str]
	"""
	if len(s) == 0: return []

	else: 
		mapping = {
		"2" : "abc", 
		"3" : "def", 
		"4" : "ghi", 
		"5" : "jkl", 
		"6" : "nmo", 
		"7" : "pqrs", 
		"8" : "tuv", 
		"9" : "wxyz"
		}
		output = [ i for i in mapping[s[0]] ]
		s = s[1:]
		temp = []
		while s != "":
			for comb in output:
				for char in mapping[s[0]]:
					temp.append(comb + char)
			output = temp
			temp = []
			s = s[1:]
	return output

"""
Given a list of intervals, make it so that that there are no overlaps.
Example: [[1, 3], [2, 5], [6, 9]] -> [[1, 5], [6, 9]]
"""

def merge_intervals(l):
	"""
	:type l: List[List[int]]
	:rtype: List[List[int]]
	"""
	sorted_list = []

	# Ensure that intervals are sorted; takes O(nlogn) time
	while l:
		EFT, pos = float("inf"), float("inf")
		for i, item in enumerate (l):
			if item[1] < EFT:
				EFT, pos = item[1], i
		sorted_list.append(l.pop(pos))

	# Merge the intervals; takes O(n) time
	merged_list = []
	for item in sorted_list:
		# If end-time is less that next interval start-time, just append
		if not merged_list or merged_list[-1][1] < item[0]:
			merged_list.append(item)

		else:
			merged_list[-1][1] = item[1]

	return merged_list

"""
Given a list of intervals, insert a new interval into it
Example: [[1, 3], [2, 5], [6, 9]] + [3, 8] -> [[1, 9]]
"""

def insert_interval(L1, new_interval):
	"""
	:type L1: List[List[int]]
	:type new_interval: List[int]
	:rtype: List[List[int]]
	"""
	return merge_intervals(L1 + [new_interval])


