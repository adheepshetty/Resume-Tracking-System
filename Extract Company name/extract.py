import csv
import json
from fuzzywuzzy import fuzz

with open('college.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list1=[]
    val=""
    for row in csv_reader:
        if line_count == 0:
            print(row[0])
            line_count += 1
        else:
        	if fuzz.ratio(val, row[1])<60:
        		print(row[1])
        		list1.append(row[1])
        		line_count += 1
        		val=row[1]
    print(line_count)
    with open('college.txt', 'w') as outfile:
    	json.dump(list1, outfile)
