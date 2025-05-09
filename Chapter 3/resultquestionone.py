passes = 0
failures = 0
count = 1
result = 0

for student in range(10):
	result = int(input("Enter result (1 and 2 =pass): "))
	if result == 1:
		passes = passes + 1
	else:
		faliures = failures + 1

print("Passed: ", passes)
print("Failed: ", failures)

if passes > 8:
	print("Bonus to instructor")