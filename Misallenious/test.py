import re

filename='baby1990.html'
f=open(filename,'rU')
line=f.read()
year_match=re.search('Popularity\sin\s(\d\d\d\d+)',line)

if year_match:
	print year_match.group()


print year_match.group(1)

##rank and names in a touple

name_match=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)

det_dic={}


for lines in name_match:
	(year,bname,gname)=lines	
	fout=open('out.txt','a')
	fout.write(year+' '+ bname+' '+gname+'\n')
