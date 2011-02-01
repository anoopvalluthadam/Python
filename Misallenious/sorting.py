str=['zc','yb','ra','wd']

def MyFunc(s):
	return s[-1] 
print sorted(str,key=MyFunc)
