f=open('wcount.py','r')
string=f.read()




splited= string.split()


real=[]
for i in splited:
	real.append(i.lower())

##print real


r_removed=[]

for words in real:
	if words not in r_removed:
		r_removed.append(words)

dic={}
for words in r_removed:
	dic[words] = ' '
count=0
##print dic


for words in dic:
	for i in real:
		if words==i:
			count=count+1
			dic[words]=count
	count=0

##print '------------------------------'
##print dic
##print '-------------------------------'

s=[]
for i in dic.items():
	s.append(i)

##print s

def sorting(s):
	return s[-1]


sorted_dic=sorted(s,key=sorting)

print sorted_dic[::-1]
