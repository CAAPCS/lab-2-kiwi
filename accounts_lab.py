class Accounts:
    def __init__(self, type):
        self.balance = 0
        self.type = type
class checkingAccounts(Accounts):
    pass
class savingsAccounts(Accounts):
    def appliedDailyInterest(date):
        dates.append(date):
        power = int(date) - int(dates[len(dates) - 2])
        b = 0
        while b < len(accounts):
            if(accounts[b].type.casefold() == 'SAVINGS'.casefold()):
                accounts[b].balance = round(accounts[b].balance*(1.0001**power), 2)
            b += 1
        pass
class creditAccounts(Accounts):
    pass

def DEPOSIT(name, date, money):


def WITHDRAW(name, date, money):
