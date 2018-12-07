#!/usr/bin/env python3
from string import ascii_lowercase


input_file = "inputs/input_05.txt"

def react_polymer(polymer):
	polymer_list = list(polymer)

	while(True):
		length = len(polymer_list)

		for i in range(0, length-1):
			c1 = polymer_list[i]
			c2 = polymer_list[i+1]

			if c1.lower() == c2.lower() and c1 != c2:
				polymer_list[i] = ""
				polymer_list[i+1] = ""

		polymer_stripped = [x for x in polymer_list if x]
		if(len(polymer_stripped) != length):
			polymer_list = polymer_stripped
			continue
		
		return length


def q1():
	# Answer: 10978
	with open(input_file) as f:
		polymer = f.read()
		return react_polymer(polymer)


def q2():
	# Answer: 4840
	with open(input_file) as f:
		polymer = f.read()
		lengths = {}

		for c in ascii_lowercase:
			polymer_modified = polymer.replace(c, '').replace(c.upper(), '')
			lengths[c] = react_polymer(polymer_modified)

		print(lengths)
		return min(lengths.values())


if __name__ == '__main__':
	print("Answer for part 1:", q1())
	print("Answer for part 2:", q2())