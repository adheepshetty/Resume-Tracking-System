import json
import pandas as pd

list2=[]
dic={}
with open('data.json') as json_file: 
	list2 = json.loads(json_file.read())
	for i in list2:
		list3=i['jobs']
		for j in list3:
			if not j['title'] in dic:
				dic[j['title']]+=1
				p




