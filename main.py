import sys
from bank import Bank

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
