investment_amount = int(input("Enter the investment amount: "))

number_of_years  = int(input("Enter the number of years: "))

interest_rate  = float(input("Enter interest rate: "))

returnoninvestment = 0
percentagerate = interest_rate / 100

for years in range(1, number_of_years+1):
	returnoninvestment = investment_amount * ((1 + percentagerate) ** (years)) 
	print(f"The return of investment for year {years} is {returnoninvestment:.2f}")
	