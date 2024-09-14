import unittest
from bank_account import BankAccount

# INIT TEST CLASS
class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.bank_account = BankAccount("4843985", 500.00)
    
    def test_get_account_number(self):
        self.assertEqual(self.bank_account.get_account_number(), "4843985")

    def test_get_balance(self):
        self.assertEqual(self.bank_account.get_balance(), 500.00)

    def test_deposit(self):
        account = BankAccount("4843985", 500.00)
        account.deposit(500.00)
        self.assertEqual(account.get_balance(), 500.00)
    
    def test_deposit_negative_amount(self):
        account = BankAccount("4843985", 500.00)
        account.deposit(-50.0)
        self.assertEqual(account.get_balance(), 500.00)
    
    def test_deposit_zero_amount(self):
        account = BankAccount("4843985", 500.00)
        account.deposit(0.0)
        self.assertEqual(account.get_balance(), 500.00)
    
    def test_withdraw(self):
        account = BankAccount("4843985", 500.00)
        account.withdraw(50.0)
        self.assertEqual(account.get_balance(), 450.0)
    
    def test_withdraw_negative_amount(self):
        account = BankAccount("4843985", 500.00)
        account.withdraw(550.00)
        self.assertEqual(account.get_balance(), 500.00)
    
    def test_withdraw_zero_amount(self):
        account = BankAccount("4843985", 500.00)
        account.withdraw(0.0)
        self.assertEqual(account.get_balance(), 500.00)


    if __name__ == '__main__':
        unittest.main()