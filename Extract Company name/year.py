import re

str = "cd"
pair = re.compile(r".*([1-2][0,9][0-9]{2})")
x = pair.findall(str)
if len(x)>0:
	
print(x)