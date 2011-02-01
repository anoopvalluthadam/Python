str=u'asdjfhjasfd \u019e string \xf1'
print str
print ("\n\n")

s=str.encode('utf-8')
print s

t = unicode(s,'utf-8')
print ("\n"+t)
