names={"Anoop":2,"Valluthadam":4}
try:
		if names["Anoo"] >=2:
			print ("hi")
except (KeyError) as error:
	print("Error is '%s'" %error)