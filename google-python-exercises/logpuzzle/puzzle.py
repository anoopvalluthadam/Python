import re
import urllib


src='place_code.google.com'

f=open(src,'r')
line=f.read()

##l_lines=[]

str=re.findall(r'GET\s(.*).jpg\sHTTP',line)

l_url=[]

for lines in str:
	url=lines+'.jpg'
	l_url.append(url)	


l_url2=[]



def sorting(s):
	return s[-8:]


for i in l_url:
	if i not in l_url2:
		l_url2.append(i)

print l_url2

sorted_list=sorted(l_url2, key=sorting)



f=open('index.html','w')
f.write('<html><body>')


i=0
for url in sorted_list:
	img_name='img%d' % i

	final_url='http://code.google.com'+url
	file=urllib.urlretrieve(final_url,'/home/gabriel/Pictures/'+img_name+'.jpg' )
	print file
	f.write('<img src="/home/gabriel/Pictures/'+img_name+'.jpg">')
	i=i+1	

f.write('"</body></html>')


