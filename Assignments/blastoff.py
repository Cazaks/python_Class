

while True:
	n = int(input("Enter any number: "))
	if n < 0:
		print("Invalid selection, enter a valid number")
		
	for numbers in range(n, 0, -1):
		print(numbers)
	print("Blast off!")

	break