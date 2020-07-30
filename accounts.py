class accounts:
    def __init__(self, acctNum, name, type):
        self.name = name
        self.acctNum = acctNum
        self.type = type
        self.balance = 0
        self.accountHistory = []

    def withdrawing(self, amount):
        prior_balance = self.balance
        self.balance -= amount
        self.accountHistory.append(transactions(amount, date, prior_balance, self.balance))


    def depositing(self, amount):
        prior_balance = self.balance
        self.balance += amount
        self.accountHistory.append(transactions(amount, date, prior_balance, self.balance))

    def accountInfo(self):
        for trans in self.accountHistory:
            print(str(trans.name) + ";" + (str(trans.type) + ";" + (str(trans.date) + ";"+ str(trans.amount))

    def balanceInquery(self):
        return self.balance


class checkingAccounts(Accounts):
    pass
class savingsAccounts(Accounts):
    def appliedDailyInterest(date, amount):
        self.balance -= (amount * 1.0001)
    pass
class creditAccounts(Accounts):
    pass
