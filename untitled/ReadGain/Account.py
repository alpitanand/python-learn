import datetime
import pytz


class Accounts(object):

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for {} with balance {}".format(name, balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        self.transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount

    def show_balance(self):
        print("The balance for {} is {}".format(self.name, self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                print("Deposited")
            print("{} {}".format(date, amount))


if __name__ == "__main__":
    Alpit = Accounts("Alpit", 0)
    Alpit.deposit(10000)
    Alpit.show_transaction()
    Alpit.show_balance()
    Alpit.withdraw(2309)
    Alpit.show_balance()
    Prachee = Accounts("Prachee", 10000)
    Prachee.deposit(1000)
    Prachee.withdraw(213)
    Prachee.balance = 10000
    Prachee.show_transaction()
    print(Prachee.__dict__)
    print(Prachee.__dict__['name'])
