principal = 1000
rate = 0.05

for year in range(1, 31):
	amount = principal * (1 + rate) ** year 
	print(f"For year {year:>2} the amount will be: {amount:>10.2f}")
