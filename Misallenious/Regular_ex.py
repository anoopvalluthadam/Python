import re

str="Hello this is just a test File for testing Regular expressoin"
f=re.search(r'this \w\w',str)
if f:
	print "Match Found : %s",%f
else:
	print "Not Found"
