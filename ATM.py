from cmath import pi


class ATMUser:
    def __init__(self, balance, pin, card):
        self.balance = int(balance)
        self.pin = int(pin)
        self.card = int(card)
    
    def withdrawCash(self):
        w = int(input("How much money would you like to withdraw? "))
        if self.balance >= w:
            print("Loading...")
            print("Withdrawal is Succsesful for", w, "dolars")
            finalWithdraw = self.balance - w
            print("You have", finalWithdraw, "dollars in your account")
        else:
            print("You don't have enough money in your account to withdraw", w)


    def depositCash(self):
        d = int(input("How much money would you like to deposit? "))
        print("Loading...")
        print("Deposit is Succsesful for", d, "dollars")
        finalDeposit = self.balance + d
        print("You have", finalDeposit, "dollars in your account")

    def checkBalance(self):
        print("You have", self.balance, "dollars in your account")

y = input("Please Enter Pin Number: ") 
z = input("Please Enter ATM Card Number: ")    
Ex = ATMUser(1500, y, z)


print("1 = Withdraw, 2 = Deposit, 3 = Check Balance")
x = int(input("Type in the Number Corresponding to the Action That You Would Like To Do: "))
if x == 1:
    Ex.withdrawCash()
  
elif x == 2:
    Ex.depositCash()

elif x == 3:
    Ex.checkBalance()

else:
    print(x, "is not one of the options, please try again")