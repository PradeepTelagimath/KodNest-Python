class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_holder(self):
        return f"Account Holder: {self.account_holder}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        # Call the parent constructor using super()
        super().__init__(account_holder)
        # Store balance in the child object
        self.balance = balance

    def show_balance(self):
        # Return the balance formatted to match the output
        return f"Balance: {self.balance}"


name = input()
balance = int(input())

account = SavingsAccount(name, balance)

print(account.show_holder())
print(account.show_balance())