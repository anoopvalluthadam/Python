import re

str='adsfadf anoop_valluthadam@gmail.com,jshdg mut-antchernoboyl@gmail.com'
touple=re.findall(r'([\w-]+)@([\w.]+)',str)
print touple
print "\n------------------------------------------\n"
for i in touple:
	print i[0]
	print i[1]
