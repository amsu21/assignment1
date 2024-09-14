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