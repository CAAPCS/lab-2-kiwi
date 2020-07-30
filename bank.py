from transactions import transactions
from customers import customers
from accounts import accounts

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
