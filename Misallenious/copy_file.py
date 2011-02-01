#!/usr/bin/python

import shutil
import os
import sys
import gzip


def main():
	


	args=sys.argv[1:]

	if not args:
		sys.exit()
	
	print args[0]
	print args[1]
	
	src=args[0]
	dst=args[1]

	f=shutil.copy(src,dst)

	print f

	zsrc=args[2]
	f=gzip.open('/home/gabriel/test.py.gz','wb')
	f.write(zsrc)	




main()
