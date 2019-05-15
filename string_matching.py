from fuzzywuzzy import fuzz
import json

list1=[]
with open('company_name.txt') as file:
	list1=json.load(file)

max=0
str1=""

company_name="in Engineering"

company_name.replace("MS", "Master")
company_name.replace("BS", "Bachelor")
master="Bachelor"
for i in ["Master","Bachelor"]:
	val=fuzz.ratio(company_name, i)
	print(val)
	if val>max:
		max=val
		master=i

max=0

for i in list1:
	val=fuzz.ratio(company_name, i)
	if val>max:
		max=val
		str1=i


print(master)
