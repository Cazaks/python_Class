atmConsoles = """
Welcome to Semicolon bank
press;
1 - To enter balance
2 - To withdraw money
3 - Display amount
4 - Multiple withdrawal
5 - Transaction details
0 - To Exist
"""
consoleSelect = True
while consoleSelect:
	print(atmConsoles)
	select = int(input('enter a number to select: '))
	match select:
		case 0:
			consoleSelect = False
		case 1:
			balancemenu = True
			while balancemenu:
				Enterbalance = amount = int(input('enter amount: '))
				print("Your balance is:", amount)
				#match amountmenu:
					
						#balancemenu = False
		case 2:
			Withdrawmoney = True
			while Withdrawmoney:
				required_amount = balance = int(input("Enter amount to withdraw: "))
				balance = (balance / 100) * 90
				if balance % 500 == 0:
					print("Transaction Successful")
					print("The amount withdrawn is: ", required_amount)
				if balance < 0:
					print("withdrawal amount must be positive")
				if balance <= 99:
					print("Balance must be N100 and above")
				if amount > balance:
					print("Insufficient balance")
				if amount % balance and balance <= 20_000:
					print("transaction successful")
		
		case 3:
			print()
			accountdetails = True
			while accountdetails:
				


			
