import codecs

f=codecs.open('text.txt','rU','utf-8')
for line in f:
	print line
