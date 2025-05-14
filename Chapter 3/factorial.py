number = int(input("Enter an integer: "))

factorial = 1

for counter in range(1, number + 1):
	factorial = factorial * counter

print(f"The factorial of {number} is: {factorial}")