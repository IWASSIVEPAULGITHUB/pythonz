#A bankaccount class program
class Bankaccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

account = Bankaccount(123456, "Joshua Waweru", 30000, "2008-08-19")
print(account.deposit(10000))  # Deposited: 10,000
print(account.withdraw(5000))  
account.check_balance()  
account.customer_details()
