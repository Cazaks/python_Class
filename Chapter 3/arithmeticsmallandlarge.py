product = 1
largest = 0
smallest = 0
sum = 0
for number in range(4):
	digit = int(input("Enter a four digit integers: "))

	sum =  sum + digit 
	product = product * digit

	if number > largest:
		largest = number

	if number < smallest:
		smallest = number

average = sum / 4



print(f"The sum of the numbers is: {sum}")
print(f"The average of the numbers is: {average}")
print(f"The product of the numbers is: {product}")
print(f"The largest is: {largest}")
print(f"The smallest is: {smallest}")