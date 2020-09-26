# Define Class BankAccount
class BankAccount:
    # initialize balance to 0
    def __init__(self, name, balance=0.0):
        self.log('Account Created!')
        self.name = name
        self.balance = balance
    
    def get_balance(self):
        self.log('Balance Checked at ' + str(self.balance))
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.log('+' + str(amount) + ': ' + str(self.balance))
    
    def withdraw(self, amount):
        self.balance -= amount
        self.log('-' + str(amount) + ': ' + str(self.balance))
    
    def log(self, log_msg):
        log_file = open(r'Chapter_5.1_Objects\\Examples\\log2.txt', 'a')
        print(log_msg, file=log_file)
        log_file.close()

sam_acc = BankAccount('Sam')
sam_acc.deposit(20.0)
print(sam_acc.get_balance())
sam_acc.withdraw(10.0)
print(sam_acc.get_balance())