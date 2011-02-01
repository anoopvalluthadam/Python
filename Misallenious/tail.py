
f=open('Func.py','r')
list=[]
s=f.readlines()
for i in s:
	
	line=i.rstrip()
	list.append(line)
length=len(list)
#print length

if length>10:
	print list[length-11:]
else:
	i=0
	while i<length:
		print list[i]
		i=i+1
