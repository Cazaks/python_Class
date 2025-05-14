numbers = 0
first_largest = 0
second_largest = 0

for numbers in range(10):
	numbers = int(input("Enter an integer: "))
	if numbers > first_largest:
		second_largest = first_largest
		first_largest = numbers
	elif numbers > second_largest: 
		seccond_largest = numbers

print(f"The first largest number is: {first_largest}")
print(f"The second largest number is: {second_largest}")

		
