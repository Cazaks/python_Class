class Bankaccounts:
	def _init_(self, phone_number, account_holder, balance=0):
		self.phone_number = phone_number
		self.account_holder = account_holder
		self.balance = balance

	def create_account(self, name, phonenumber):
		if phonenumber == self.phone_number:
			print('Account already exist')
		else:
			print('Account successfully created')
	
	def make_a_deposit(self, deposit_amount):
		if deposit_amount <= 0:
			print("You cannot deposit a negative or 0 amount")
		elif amount > 0:
			self.balance = self.balance + deposit_amount
			print(f'The aount deposited is {deposit_amount} and your balance is {balance})

	def make_withdrwal(self, withdrawal_amount):
		if withdrawal_amount <= 0:
			print("You cannot withdraw a negative or 0 amount")
		elif amount > 0:
			self.balance = self.balance + deposit_amount
			print(f'The aount deposited is {deposit_amount} and your balance is {balance})
	if amount < bal:
		bal -= amount
		return bal

def make_tranfer(amount, name, bal):
	if amount > bal:
		print("Insufficient balance")
	if amount < 0:
		Print("Tansfer cannot be negative")
	if amount < bal:
		return bal		
	

def main():
	while True:
		print("\naccountbalance")
		print("1. Create account")
		print("2. Make a deposit")
		print("3. Make withdrwal")
		print("4. Make tranfer")
		print("0. T0 exit")

userchoice = input("Choice an option: ")
if userchoice == "1":
	create_account()
if userchoice == "2":
	make_a_deposit()
if userchoice == "3":
	make_withdrwal()
if userchoice == "4":
	make_transfer()
if userchoice == "0":
	print("Good bye")
if _name_== " _main_":
	main()	
	

#name = input("Enter your name: ")
#phonenumber = input("Enter phone number: ")
#create_account(name, phonenumber)