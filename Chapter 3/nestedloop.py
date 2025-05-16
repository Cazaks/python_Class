printing = 10
for star in range(printing): 
	for asteric in range(star + 1):
		print("*", end="")

	print()

print()
printing = 10
for star in range(printing): 
	for asteric in range(star, printing):
		print("*", end="")

	print()

printing = 10
for star in range(printing):
	print(" ", end="") 
	for asteric in range(star+1):
		print(" ", end="") 	
	for asteric in range(star, printing):
		print("*", end="")
	
	print()

print()
printing = 10
for star in range(printing):
	print(" ", end="") 
	for asteric in range(star, printing):
		print(" ", end="") 	
	for asteric in range(star + 1):
		print("*", end="")
	
	print()


