def function(s,condition):
	result=s+s+s
	if condition:
		result=result+'!!!'
	return result

def main():
	print function('Yay',False)
	print function ('Whooo',True)

if __name__=='__main__':
	main()
