dictionary={"a":"Allen Donald","c":"catich","b":"Badarinath","d":"Dhoni"}
print dictionary.keys()

for key in dictionary.keys():
	print dictionary[key]

print ("\n-----------------------Sorted Dictionary------------------\n")
for i in sorted(dictionary.keys()):
	print i
	print dictionary[i]
print dictionary.items()
