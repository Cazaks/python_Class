from banking import Bank

def main():
    bank = Bank()
    print("Welcome to AdeyemiBank!")

    while True:
        print("\nOptions:")
        print("1 - Create account")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Find customer")
        print("5 - List all customers")
        print("6 - Exit")

        choice = input("Choose option: ")

        if choice == '1':
            name = input("Your name: ")
            phone = input("Your phone: ")
            try:
                account = bank.create_account(name, phone)
                print(f"Account created! Your account number is {account.account_number}")
            except ValueError as e:
                print("Error:", e)

        elif choice == '2':
            try:
                acc_num = int(input("Account number: "))
                amount = float(input("Amount to deposit: "))
                bank.deposit(acc_num, amount)
                print("Deposit successful.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                acc_num = int(input("Account number: "))
                amount = float(input("Amount to withdraw: "))
                bank.withdraw(acc_num, amount)
                print("Withdrawal successful.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            method = input("Find by (1) Account Number or (2) Phone? ")
            if method == '1':
                try:
                    acc_num = int(input("Enter account number: "))
                    acc = bank.find_by_account_number(acc_num)
                    print(f"Owner: {acc.owner}, Phone: {acc.phone}, Balance: {acc.balance}")
                except Exception as e:
                    print("Error:", e)
            elif method == '2':
                phone = input("Enter phone: ")
                try:
                    acc = bank.find_by_phone(phone)
                    print(f"Owner: {acc.owner}, Account Number: {acc.account_number}, Balance: {acc.balance}")
                except Exception as e:
                    print("Error:", e)
            else:
                print("Invalid option.")

        elif choice == '5':
            customers = bank.list_customers()
            if not customers:
                print("No customers yet.")
            else:
                for c in customers:
                    print(f"Account: {c.account_number}, Owner: {c.owner}, Phone: {c.phone}, Balance: {c.balance}")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option.")

if _name_ == "_main_":
    main()