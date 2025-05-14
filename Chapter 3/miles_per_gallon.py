total = 0
gallons_counter = 0
gallons_used = float(input("Enter gallons used, enter -1 to end: "))
miles_driven = int(input("Enter miles driven: "))

while gallons_used != -1 or miles_driven != -1: 
	if gallons_used == -1 or miles_driven == 1:
		break
	miles_gallons = miles_driven / gallons_used
	total = total + miles_gallons
	gallons_counter = gallons_counter + 1
	gallons_used = float(input("Enter gallons used, enter -1 to end: "))
	miles_driven = int(input("Enter miles driven: "))

if gallons_counter != 0:
	average = total / gallons_counter
	print("The average is: ", average) 


