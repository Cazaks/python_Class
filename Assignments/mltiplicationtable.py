print("Multiplication Table")
for count in range(1, 10):
	print(f"{count:>6}", end=' ')

print("\n-----------------------------------------------------------------")
for values in range(1, 10):
	print(values)

for i in range (1, 10):
	for j in range (1, 10):
		table = i * j
		print(f"{table: >6}", end=' ')
	
	print()
