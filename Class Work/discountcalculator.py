

amount = int(input("Enter purchase amount: "))

fivepercent = 0.05
tenpercent = 0.10
twentypercent = 0.20

if amount < 1000
	print("Invalid selection, try again.")

if amount >= 1000 and amount <= 10000:
	purchasediscount = float(amount * fivepercent)
	discount = float(amount - purchasediscount)
	print(f"Your 5% discount is: {discount}")
	print(f"You have {purchasediscount} from your discount")

if amount > 10000 and amount <= 50000:
	purchasediscount = float(amount * tenpercent)
	discount = float(amount - purchasediscount)
	print(f"Your 10% discount is: {discount}")
	print(f"You have {purchasediscount} from your discount")

if amount > 50000:
	purchasediscount = float(amount * twentypercent )
	discount = float(amount - purchasediscount)
	print(f"Your 20% discount is: {discount}")
	print(f"You have {purchasediscount} from your discount")




	