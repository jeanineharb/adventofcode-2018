#!/usr/bin/env python3
from collections import Counter
import difflib


input_file = "inputs/input_02.txt"

def q1():
	# Answer: 7105
	occurrences = {}

	with open(input_file) as f:
		for line in f:
			counter = Counter(line)
			occ_set = set(counter.values())

			for v in occ_set:
				if(occurrences.get(v) is None):
					occurrences[v] = 1
				else:
					occurrences[v] += 1

	print(occurrences)
	occurrences.pop(1, None)

	checksum = 1
	for _, o in occurrences.items():
		checksum *= o

	print("Checksum:", checksum)


def q2():
	# Answer: omlvgdokxfncvqyersasjziup
	with open(input_file) as f:
		lines = f.read().splitlines()
		index = 0

		for l1 in lines:
			for l2 in lines[index+1:]:
				diff_list = [li for li in difflib.ndiff(l1, l2) if li[0] != ' ']

				if len(diff_list) == 2:
					print(l1)
					print(l2)
					print(diff_list)

					common_letters = l1.replace(diff_list[0][-1], "")
					print("Common letters:", common_letters)
					return

			index += 1


if __name__ == '__main__':
	q2()