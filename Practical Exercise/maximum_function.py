def maximum(value1, value2, value3):
	maximum_number = value1
	if value2 > maximum_number:
		maximum_number = value2

	if value3 > maximum_number:
		maximum_number = value2

	return maximum_number

print(maximum(23, 43, 34))

