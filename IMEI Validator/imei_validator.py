number = input("Enter number: ")

def check_IMEI(n):
	numList = []
	str_num = str(n)

	# Creating new list to store number
	for num in str_num:
		numList.append(int(num))

	# Doubling every two numbers

	doubled = numList
	for eachnum in range((len(numList)-2),0,-2):
		doubled[eachnum] = (numList[eachnum]*2)

	# Add each number from the doubled list
	doubled_num = int(''.join(str(dbl_num) for dbl_num in doubled))
	doubled_num = str(doubled_num)

	sum_list = []

	total = (sum(int(x) for x in doubled_num))
	if (total % 10) == 0:
		return True
	else:
		return False
if check_IMEI(number):
	print("Valid.")
else:
	print("Invalid.")
