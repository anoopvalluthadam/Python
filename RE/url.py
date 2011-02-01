import re


str="/asd/asd/e/wer/asjdhf/p-asd-heu-hyu.jpg"

print str

str1=re.search(r'(.*)-(\w+).jpg',str)

print str1.group(2)
