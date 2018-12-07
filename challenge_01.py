#!/usr/bin/env python3
input_file = "inputs/input_01.txt"

def q1():
	# Answer: 580
	with open(input_file) as f:
		total = 0
		for line in f:
			op = line[0]
			nb = int(line[1:])

			if op == "-":
				total = total - nb
			else:
				total = total + nb

		print("Total of frequencies:", total)

def q2():
	# Answer: 81972
	total = 0
	history = []
	repeat = True

	while(repeat):
		with open(input_file) as f:
			for line in f:
				op = line[0]
				nb = int(line[1:])

				if op == "-":
					total = total - nb
				else:
					total = total + nb

				if total in history:
					repeat = False
					print(total)
					break

				history.append(total)
			print("First duplicate frequency:", total)


if __name__ == '__main__':
	q1()