import sys
try:
	def main():
		print ("%s" % sys.argv[1])
	if __name__=='__main__':
		main()
except IndexError as error:
	print "please enter an argument"
