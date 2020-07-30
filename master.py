def main(fname):
    bank = Bank("Welcome to KiWi's Online Banking System!")
    print(f"{bank.bank_name} open!")
    print("Thank you for banking with KiWi's Online Banking System!")

if __name__ == '__main__':
    if len(sys.argv) != 2: #
        print("Please provide one argument, the input file")
        exit()

    arg1 = sys.argv[1] # asking first argument (another you can ask for the last argument sys.argv[-1])
    # negitive indexing for lists is reverse:
        # a = []
        # a[1] #second thing in the lst
        # a[-x] <--> a[len(a) - x)
    main(arg1)

if __name__ == '__main__':
    if len(sys.argv) != 2: #
        print("Please provide one argument, the input file")
        exit()

    arg1 = sys.argv[1] # asking first argument (another you can ask for the last argument sys.argv[-1])
    # negitive indexing for lists is reverse:
        # a = []
        # a[1] #second thing in the lst
        # a[-x] <--> a[len(a) - x)
    main(arg1)

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
                if "CREATE".casefold() in line.casefold():
                    self.customerList.append(customers(value[5], "".join(value[6:]), value[2], value[4], value[3]))
                else:
                    for victim in self.customerList:
                        if (victim.account.type == "savingsAccounts"):
                            victim.account.appliedDailyInterest()
                        if value[2].casefold() in line.casefold()
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
        self.date = date
        self.balance -= (amount * 1.0001)
    pass
class creditAccounts(Accounts):
    pass
