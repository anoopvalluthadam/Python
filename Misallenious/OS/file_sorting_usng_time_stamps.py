import os
import os.path
import time

content = {}
for item in os.listdir('.'):
    content[item] = os.path.getmtime(item)
items = content.keys()
items.sort(lambda x,y:cmp(content[x],content[y]))
for item in items:
    print '%15s %s' %(item, time.ctime(content[item]) )
