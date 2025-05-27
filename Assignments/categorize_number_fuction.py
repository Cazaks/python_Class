def categorize_number(*numbers, divisor=2):
	nums = []
	for num in numbers: 
		if num % divisor == 0:
			nums.append(num)
		return num

value1 = 22
value2 = 12
value3 = 10
value4 = 16
print(categorize_number(value1, value2, value3, value4))