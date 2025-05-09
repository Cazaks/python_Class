investment_amount = int(input("Enter the investment amount: "))

number_of_years  = int(input("Enter the number of years: "))

interest_rate  = int(input("Enter interest rate: "))
counter = 0
return_on_investment = 0
percentage = 100
interest = interest_rate / percentage
year = 0

while counter != number_of_years:
	percentageamount = investment_amount *  interest
	return_on_investment += investment_amount + percentageamount 
	counter+=1
	print(f"The return of investment for year {year} is {return_on_investment:.2f}")