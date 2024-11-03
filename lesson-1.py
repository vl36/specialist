acc1 = {"name": "Petya", "balance": 200, "currency": "RUB"}
acc2 = {"name": "Vasya", "balance": 400, "currency": "RUB"}
changes: int = 100
print(acc1, acc2)

# test 1
acc1["balance"] -= changes
acc2["balance"] += changes
print(acc1, acc2)


# test 2
def transfer(payer, recipient, amount):
    if amount <= payer["balance"]:
        payer["balance"] -= amount
        recipient["balance"] += amount
    else:
        print("wrong amount")


transfer(acc1, acc2, changes)
print(acc1, acc2)


# test 3
class DebitAccount:
    def __init__(self, name=" ", balance=0, currency="RUB"):
        self.name = name
        self.balance = balance
        self.currency = currency

    def recive(self, amount):
        if amount > 0:
            self.balance += amount
            return 0
        else:
            print("Recive ERROR")
            return -1

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
        else:
            print("Transfer ERROR")


account1 = DebitAccount("Petya", 3000)
account2 = DebitAccount("Vasya", 4000)

account1.recive(500)
print(account1.balance)
account1.transfer(account2, 200)
print(account1.balance)
print(account2.balance)
