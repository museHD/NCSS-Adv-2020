def is_ab(num):
	num_str = str(num)
	freq = {}
	revfreq = {}
	#  Going through the string and storing the frequency of each char in 'freq'
	for digit in num_str:

		revfreq[num_str.index(digit)] = digit

		if digit in freq:
			freq[digit] += 1
		else:
			freq[digit] = 1

	for x in range(len(num_str)):

		this_digit = num_str[x]
	# Checking if the each digit in the input number corresponds with the frequenc off digits
		if freq.get(str(x),0) == int(this_digit):
			print('yes')
		else:
			print('no')

is_ab()

