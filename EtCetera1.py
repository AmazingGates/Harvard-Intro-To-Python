# In this section we will be talking about the keyword "global". This keyword allows us to tell a function that 
#we intend for a certain "variable" to be "global", and not "local".
balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n
    

if __name__=="__main__":
    main()


# In the example below we will be working the same code as above, but instead we will code it diffferently.
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__=="__main__":
    main()