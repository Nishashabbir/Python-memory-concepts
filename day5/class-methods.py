
# real program on system level as well as  object level methods and fetching of data 

class BankAccount:
    total_accounts = 0
    total_money_in_bank = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
        BankAccount.total_accounts += 1
        BankAccount.total_money_in_bank += balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.total_money_in_bank += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            BankAccount.total_money_in_bank -= amount
        else:
            print("Insufficient funds!")

    @classmethod
    def bank_status(cls):
        return f"Total Accounts: {cls.total_accounts}, Total Money: {cls.total_money_in_bank}"

    @classmethod
    def from_string(cls, data_str):
        owner, balance = data_str.split(",")
        return cls(owner.strip(), float(balance.strip()))
    

# now this is how we actually use it 
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

acc1.deposit(500)

print(BankAccount.bank_status())  #this is how we are getting the information on system level (through class methods )
print(acc1.owner , ": ")  #this will just check the money of one account not all 
print(acc1.balance) 