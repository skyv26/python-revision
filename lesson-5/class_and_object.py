'''

  Let's solve our challenge of the lesson, I will make sure that you will 
  practice all previous lesson things into the problems, we are going 
  to extend the requirement for exploring the possibilities and regain our 
  past knowledge
'''

from datetime import datetime

class BankAccount:
    def __init__(self, name, balance=0):
        self.owner_name = name
        self.balance = balance
        self.transactions = []
    
    def transaction_obj(self, amount, type='deposit'):
        new_dictionary = {
            "amount": amount,
            "type": type,
            "created_at": datetime.now(),
        }
        self.transactions.append(new_dictionary);

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.message(f"Amount ${amount} deposit successfully !!\nYour new balance: ${self.balance}")
            self.transaction_obj(amount)
        else:
            print('Amount can\'t be negative to deposit')
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.message(f"Amount {amount} withdraw successfully !!\nYour new balance: {self.balance}")
            self.transaction_obj(amount, 'withdraw')

        else:
            print(f'Sorry! Your have insufficient balance : ${self.balance}')
    
    def message(self, msg):
        print(msg)
    
    def show_balance(self):
        return f"Your balance : ${self.balance}" # Getting the latest `balance` value

    def mini_statement(self):
        print('\n\nMini Statment\n=============')
        for each in self.transactions: # Iterating over the transactions dictionary created in the constructor
            if each['type'] == 'deposit':
                self.message(f"{each['created_at']} You deposited +${each['amount']} amount")
            elif each['type'] == 'withdraw':
                self.message(f"{each['created_at']} You withdraw -${each['amount']} amount")

user_bank_account = BankAccount('Tom', 500)

# print balance
print(user_bank_account.show_balance())

# deposit money
user_bank_account.deposit(245)

# deposit money with wrong value
user_bank_account.deposit(-245)

# withdraw money
user_bank_account.withdraw(500)

# withraw money more than actual balance
user_bank_account.withdraw(2500)

user_bank_account.mini_statement()