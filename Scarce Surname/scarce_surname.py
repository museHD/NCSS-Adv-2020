surname = input("What is your surname? ")
if surname[0].lower() == 'q':
	print("You have an extremely rare surname!")
elif "q" in surname.lower():
	print("You have a rare surname!")
else:
	print("No Qs here.")