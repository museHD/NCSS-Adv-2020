def is_ab(num):
	num_str = str(num)
	freq = {}
	revfreq = {}
	# ↓ Going through the string and storing the frequency of each char in 'freq'
	for digit in num_str:

		revfreq[num_str.index(digit)] = digit

		if digit in freq:
			freq[digit] += 1
		else:
			freq[digit] = 1
	print(freq)
	print(revfreq)
	# for x in range(len(num_str)):

	# 	print(freq[str(x)])
	# 	print(revfreq.get(freq[str(x)]))
	# 	# 2 
	# 	if freq[str(x)] == revfreq.get(freq[str(x)]):
	# 		print('yech')

	

is_ab(21200)