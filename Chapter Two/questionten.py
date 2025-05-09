number1 = int(input("Enter first enteger: "))

number2 = int(input("Enter secondt enteger: "))

number3 = int(input("Enter third enteger: "))

largest = 0
smallest = 0

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3

if number1 > number2 and number1 > number3:
	largest = number1
elif number1 < number2 and number1 < number3:
	smallest = number1

if number2 > number1 and number2 > number3:
	largest = number2
elif number2 < number1 and number2 < number3:
	smallest = number2

if number3 > number2 and number3 > number1:
	largest = number3
elif number3 < number2 and number3 < number1:
	smallest = number3

print(f"The sum of the numbers is: {sum}")
print(f"The average of the numbers is: {average}")
print(f"The product of the numbers is: {product}")
print(f"The largest is: {largest}")
print(f"The smallest is: {smallest}")