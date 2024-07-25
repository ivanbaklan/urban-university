import threading


class BankAccount(threading.Thread):

    def __init__(self):
        super().__init__()
        self.balance = 1000
        self.balance_loc = threading.Lock()

    def deposit(self, amount):
        with self.balance_loc:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.balance_loc:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")



def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()


# Deposited 100, new balance is 1100
# Deposited 100, new balance is 1200
# Deposited 100, new balance is 1300
# Deposited 100, new balance is 1400
# Deposited 100, new balance is 1500
# Withdrew 150, new balance is 1350
# Withdrew 150, new balance is 1200
# Withdrew 150, new balance is 1050
# Withdrew 150, new balance is 900
# Withdrew 150, new balance is 750