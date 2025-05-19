sum = 0
number = int(input("Enter a number between 1 and 10,000, enter -1 to end: "))
while number > 0:
	sum = sum + number % 10
	number = number // 10
	
print(sum)


