# CLASS INIT
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    # GET ACCNT NUM FUNC
    def get_account_number(self):
        return self.account_number
    
    # GET BALANCE FUNC
    def get_balance(self):
        return self.balance
    
    # DEPOSIT FUNC
    def deposit(self, amount):
        # IF AMOUNT IS GREATER THAN 0
        # ADD NEW AMOUNT TO THE BALANCE
        if amount > 0:
            self.balance = amount

    # WITHDRAW FUNC
    def withdraw(self, amount):
        # IF AMOUNT IS GREATER THAN 0 & BALANCE IS
        # GREATER THAN OR EQUAL TO AMOUNT
        # DEDEUCT THE AMOUNT FROM BALANCE
        if amount > 0 and self.balance >= amount:
            self.balance -= amount