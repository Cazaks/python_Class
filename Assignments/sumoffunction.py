def sum_number(number):
	sum = 0
	digits = 0
	if number >= 1 and number <= 10_000:	
		while number != 0:
			digits = number % 10
			sum = sum + digits
			number = number // 10			
		return sum
	else: 
		return f"Out of Bounds"
		
number = 9_878
result =  sum_number(number)
print(result)
