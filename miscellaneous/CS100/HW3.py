class BankAccount:
    '''this is a BankAccount that gives each bank account its own name, account number (a string) and balance'''
    bank_name= 'Bank of America'
    def __init__(self, name, accountno, balance):
       self.name = name
       self.accountno=str(accountno)
       self.accountBalance = balance
    def deposit(self, add):
       self.accountBalance += add
       return self.accountBalance
    def withdraw(self, amount):
        self.accountBalance -= amount
        if self.accountBalance < 0:
           b = amount - self.accountBalance
           print('Warning: your account has negative balance '+ str(b))
        return self.accountBalance
           
     
    def info(self):
          print('Name:'+ self.name+'\n')
          print('Account number:'+ self.accountno+'\n') 
          print('Balance:'+ str(self.accountBalance))


