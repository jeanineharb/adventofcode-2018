#!/usr/bin/env python3
import re
import numpy as np


input_file = "inputs/input_03.txt"
regex = r"#(?P<id>\d{1,4}) @ (?P<offset_left>\d{1,3}),(?P<offset_top>\d{1,3}): (?P<w>\d{1,3})x(?P<h>\d{1,3})"

def q1():
	# Answer: 105047
	matrix = np.zeros(shape=(1000,1000))

	with open(input_file) as f:
		for line in f:
			m = re.match(regex, line)
			prop_dict = m.groupdict()
			idx = int(prop_dict["offset_left"])
			
			for i in range(int(prop_dict["w"])):
				idy = int(prop_dict["offset_top"])

				for j in range(int(prop_dict["h"])):
					if matrix[idx, idy] == 0:
						matrix[idx, idy] = prop_dict["id"]
					else:
						matrix[idx, idy] = -1

					idy +=1
				idx += 1
		
		print("Overlapping square inches:", np.count_nonzero(matrix == -1))
		return matrix


def q2():
	# Answer: 658
	matrix = q1()

	with open(input_file) as f:
		for line in f:
			m = re.match(regex, line)
			prop_dict = m.groupdict()
			
			idx_start = int(prop_dict["offset_left"])
			idy_start = int(prop_dict["offset_top"])

			idx_end = idx_start + int(prop_dict["w"]) + 1
			idy_end = idy_start + int(prop_dict["h"]) + 1

			sub_matrix = matrix[idx_start:idx_end, idy_start:idy_end]
			if -1 not in sub_matrix:
				print("ID of independant rectangle:", prop_dict["id"])
			

if __name__ == '__main__':
	q2()

