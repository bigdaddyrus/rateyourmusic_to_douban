# -*- coding: utf-8 -*-

import collections

#### This function will parse standard rym exported data to a list of dictionary keyed by first line header
def parse_exported(filename):
	linenum = 1
	columns = []
	res = []
	with open(filename) as fin:
		for line in fin:
			if linenum == 1:
				columns = line.split(",")
				columns = list(map(lambda c: c.strip(), columns))
				print columns
				if not columns:
					print ".csv file doesn't have header line."
					break
				linenum += 1
				continue

			entry = line.split(",")
			d = collections.OrderedDict()
			# get rid of the extra ""
			for z in zip(columns, entry):
				d[z[0]] = z[1].strip()[1:-1]
			res.append(d)
			linenum += 1

	print "Finished parsing {} line.".format(linenum-1)
	return res


input_filename = "input/sample_my_exported_data.csv"
parse_exported(input_filename)








