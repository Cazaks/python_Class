import unittest
from bankapp import Bank, AccountError, CustomerNotFoundError

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_create_account(self):
        account = self.bank.create_account("ade", "1234567890")
        self.assertEqual(account.owner, "ade")
        self.assertEqual(account.phone, "1234567890")
        self.assertIsNotNone(account.account_number)

    def test_deposit_and_withdraw(self):
        account = self.bank.create_account("yemi", "0987654321")
        self.bank.deposit(account.account_number, 100)
        self.assertEqual(account.balance, 100)

        self.bank.withdraw(account.account_number, 50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_more_than_balance(self):
        account = self.bank.create_account("ibrahim", "1112223333")
        self.bank.deposit(account.account_number, 30)
        with self.assertRaises(AccountError):
            self.bank.withdraw(account.account_number, 50)

    def test_find_customer(self):
        account = self.bank.create_account("bolu", "2223334444")
        found = self.bank.find_by_account_number(account.account_number)
        self.assertEqual(found.owner, "bolu")

        found_by_phone = self.bank.find_by_phone("2223334444")
        self.assertEqual(found_by_phone.owner, "bolu")

    def test_list_customers(self):
        self.bank.create_account("tife", "3334445555")
        self.bank.create_account("ope", "4445556666")
        customers = self.bank.list_customers()
        self.assertEqual(len(customers), 2)

if _name_ == '_main_':
    unittest.main()