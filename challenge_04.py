#!/usr/bin/env python3
import re
from datetime import datetime, date
import pandas as pd


input_file = "inputs/input_04.txt"

def create_history_df():
	regex = r"\[(?P<datetime>.+)\] (?P<action>\w+) (#(?P<id>\d{1,4}) \w+)?"
	data = []

	with open(input_file) as f:
		for line in f:
			m = re.match(regex, line)
			data.append(m.groupdict())

	df = pd.DataFrame.from_dict(data)
	df.sort_values(by='datetime', inplace=True)

	current_guard_id = -1
	fall_min = 0
	wake_min = 0

	history = []
	sleep = {}

	for _, row in df.iterrows():
		action, dt, guard_id = row
		dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

		if guard_id:
			if current_guard_id == -1:
				current_guard_id = guard_id
				sleep["id"] = current_guard_id

			elif guard_id != current_guard_id:
				history.append(sleep)
				sleep = {}
				current_guard_id = guard_id
				sleep["id"] = current_guard_id
				sleep["date"] = dt.date()
		
		else:
			if "falls" in action:
				fall_min = dt.minute
			else:
				wake_min = dt.minute
				for m in range(fall_min, wake_min):
					if sleep.get(m):
						sleep[m] += 1
					else:
						sleep[m] = 1

	history_df = pd.DataFrame.from_dict(history)
	cols = list(history_df.drop('id', axis=1).drop('date', axis=1).columns.values)
	cols_sorted = ['id', 'date'] + sorted(cols)
	history_df = history_df[cols_sorted].fillna(value=0.0)

	return history_df


def q1():
	# Answer: 39422
	history_df = create_history_df()
	cols = list(history_df.columns.values)

	group_by_id = history_df.groupby(["id"])[cols[2:]].sum()
	group_by_id["sum"] = group_by_id.sum(axis=1)
	guard_id_max = group_by_id['sum'].idxmax()
	minute_max = group_by_id.drop("sum", 1).ix[guard_id_max].idxmax()
	
	print("Guard ID:", guard_id_max)
	print("Minute of most sleep time:", minute_max)
	print("Answer:", int(guard_id_max)*int(minute_max))


def q2():
	# Answer: 65474
	history_df = create_history_df()
	cols = list(history_df.columns.values)

	group_by_id = history_df.groupby(["id"])[cols[2:]].sum()
	minute_frequent = group_by_id.max().idxmax()
	guard_id_frequent = group_by_id.max(axis=1).idxmax()

	print("Guard ID:", guard_id_frequent)
	print("Minute of most frequent sleep time:", minute_frequent)
	print(int(minute_frequent)*int(guard_id_frequent))


if __name__ == '__main__':
	q1()