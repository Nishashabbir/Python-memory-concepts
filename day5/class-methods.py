class BankAccount:
    total_accounts = 0
    total_money_in_bank = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
        BankAccount.total_accounts += 1
        BankAccount.total_money_in_bank += balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            BankAccount.total_money_in_bank += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            BankAccount.total_money_in_bank -= amount
        else:
            print("Invalid or insufficient funds!")

    @property
    def balance(self):
        return self.__balance

    @classmethod
    def bank_status(cls):
        return f"Total Accounts: {cls.total_accounts}, Total Money: {cls.total_money_in_bank}"

    @classmethod
    def from_string(cls, data_str):
        owner, balance = data_str.split(",")
        return cls(owner.strip(), float(balance.strip()))
    
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

acc1.deposit(500)

print(BankAccount.bank_status())
print(acc1.owner)
print(acc1.balance)   


