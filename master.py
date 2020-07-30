#DRIVER CODE#
def main(fname):
    bank = Bank("Welcome to KiWi's Online Banking System!")
    print(f"{bank.bank_name} open!")
    print("Thank you for banking with KiWi's Online Banking System!")
if __name__ == '__main__':
    if len(sys.argv) != 2: #
        print("Please provide one argument, the input file")
        exit()
    arg1 = sys.argv[1]
    main(arg1)
if __name__ == '__main__':
    if len(sys.argv) != 2: #
        print("Please provide one argument, the input file")
        exit()
    arg1 = sys.argv[1]
    main(arg1)
'''
list of days passed for interest
'''
dates = []
#BANK#
class Bank:
    def __init__(self, name_bank):
        self.name_bank
        self.accounts = []
        self.customers = []
        self.transactions = []
    def readTextFile(self):
        customerList = []
        with open("test.txt", 'r') as f:
            for line in f:
                linex = line.split(" ")
                dates.append(linex[0])
                if "CREATE".casefold() in line.casefold():
                    self.customerList.append(customers(value[5], "".join(value[6:]), value[2], value[4], value[3]))
                else:
                    for victim in self.customerList:
                        if (victim.account.type == "savingsAccounts"):
                            victim.account.appliedDailyInterest()
                        if value[2].casefold() in line.casefold():
                            if "WITHDRAW".casefold() in line.casefold():
                                victim.account.withdrawing(value[0], float(value[4]))
                            elif "DEPOSIT".casefold() in line.casefold():
                                victim.account.depositing(value[0], float(value[4]))
                            elif "BAL-INQUERY".casefold() in line.casefold():
                                 victim.account.balanceInquery()
                                 print ("Your balance is: " + victim.name + " " + victim.account.type + " " (balanceInquery))
                            elif "ACCOUNT-INFO".casefold() in line.casefold():
                                print ("\n" + victim.name + "'s recent transactions:")
                                print (victim.account.accountInfo())
#ACCOUNTS#
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
#types of accounts
class checkingAccounts(accounts):
class savingsAccounts(accounts):
    def appliedDailyInterest(date):
        self.balance *= 1.0001**(int(date) - int(dates[-2]))
class creditAccounts(Accounts):
#TRANSACTIONS#
class transactions:
    def __init__(self, day, name, prior_balance, new_balance):
        self.day = day
        self.name = name
        self.prior_balance = prior_balance
        self.new_balance = new_balance

    print("History for this account:")
    print(accountHistory[0].amount)
    self.balance += amount

    print("Balance Inquery:")
    print(balanceInquery[0].amount)
    self.balance += amount
#CUSTOMERS#
class customers:
    #Customer class encapsulates a customer in the bank. It contains the information associated with the customer.
    def CREATE(self, day, name, type, mobile, email, address,):
        self.day = date
        self.name = name
        self.type = type
        self.mobile = mobile
        self.email = email
        self.address = address
