def to_camel(ident):
	# TODO implement this function.
	# changed = ident.split()
	changed = []
	pos = -1
	makeBig = False
	for char in ident:
		pos += 1
		if char == '_':
			changed.append(ident[pos])
			makeBig = True
		elif makeBig == True:
			makeBig = False
			changed.append(ident[pos].upper())
		else:
			changed.append(ident[pos])
	changed = '_'.join(changed)
	changed = changed.replace('_','')
	return changed


if __name__ == '__main__':
  # Run the example inputs in the question.
	print(to_camel('foo'))
	print(to_camel('raw_input'))
	print(to_camel('num2words'))
	print(to_camel('num_to_SMS'))