class Customer:
    '''
    Customer class encapsulates a customer in the bank. It keeps track of their accounts and the account info
    '''
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
