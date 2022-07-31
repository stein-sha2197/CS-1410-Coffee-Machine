"""
Sharon Steinke
CS 1410
Project 4 Coffee Machine

A virtual coffee machine where user can purchase
a virtual cup of coffee or cup of chicken bouillon.

I declare that the following source code was written solely by me. 
I understand that copying any source code, in whole or in part, 
constitutes cheating, and that I will receive a zero on 
this project if I am found in violation of this policy.
"""


class CoffeeMachine:
    """
    A virtual coffee machine where user can purchase
a virtual cup of coffee or cup of chicken bouillon.

Commands:
insert currency
select number
cancel
quit

Currency:
nickel = 5
dime = 10
quarter = 25
half dollar = 50

Number:
1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon
    """
    def __init__(self, cash_box, deposit_amount, selector, products):
        self.cash_box = cash_box
        self.deposit_amount = deposit_amount
        self.selector = selector
        self.products = products

    def one_action(self):
        statement=f"""PRODUCT LIST: all 35 cents, except bouillon (25 cents)
        1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon
        Sample commands: insert 25, select 1."""
        print(statement)
        user_command = input(f'Your command: ')
        command_lyst = user_command.split(' ')
        if command_lyst[0] == 'insert':
            coin = int(command_lyst[1])
            self.deposit(coin)
            return True
        elif command_lyst[0] =='select':
            num = int(command_lyst[1])
            self.select(num)
            return True
        elif command_lyst[0] == 'cancel':
            self.return_coins()
            self.reset_deposit()
            return True
        elif command_lyst[0] == 'quit':
            return False
        else:
            error_mess = f'INVALID COMMAND.'
            print(error_mess)
            return True

    def totalCash(self):
        return self.cash_box

    #CashBox
    def deposit(self, coin):
        if coin == 50:
            self.deposit_amount += coin
            statement = f"Depositing {coin} cents. You have {self.deposit_amount} cents credit.\n"
            return print(statement)  
        elif coin == 25:
            self.deposit_amount += coin
            statement = f"Depositing {coin} cents. You have {self.deposit_amount} cents credit.\n"
            return print(statement)
        elif coin == 10:
            self.deposit_amount += coin
            statement = f"Depositing {coin} cents. You have {self.deposit_amount} cents credit.\n"
            return print(statement)
        elif coin == 5:
            self.deposit_amount += coin
            statement = f"Depositing {coin} cents. You have {self.deposit_amount} cents credit.\n"
            return print(statement)
        else:
            error_mess = f'''INVALID AMOUNT.\nWe only take half-dollars, quarters, dimes, and nickels.\n'''
            return print(error_mess)

    def return_coins(self):
        return_coins = self.deposit_amount
        if return_coins > 0:
            statement = f'Returning {return_coins} cents.'
            return print(statement)

    def deduct(self, price):
        self.deposit_amount -= price
        return self.deposit_amount

    def total(self, price):
        self.cash_box += price
        return self.cash_box
   
    def reset_deposit(self):
        self.deposit_amount = 0
        return self.deposit_amount

    #Selector
    def select(self, choiceIndex):
        if choiceIndex in range(1, 6):
            drinks = ['black', 'white', 'sweet', 'white and sweet', 'bouillon']
            drink = drinks[choiceIndex-1]
            price = self.get_price(drink)
            if price <= self.deposit_amount:
                dispense = self.make(drink)
                print(f'Making {drink}:')
                for item in dispense:
                    print(f'    Dispensing {item}')
                self.deduct(price)
                self.total(price)
                self.return_coins()
                self.reset_deposit()
                
                
            else:
                error_mess = f'Sorry. Not enough money deposited'
                return print(error_mess)
        else:
            error_mess = f'INVALID COMMAND.'
            return print(error_mess)


    #Product
    def get_price(self, drink):
        if drink == "bouillon":
            price = 25
            return price
        else:
            price = 35
            return price

    def make(self, drink):
        """
        returns recipe in a list of selected drink.
        drinks: black=1, white=2, sweet=3, white and sweet=4,
        bouillon=5.
        """
        if drink == "black":#1
            recipe = ['cup', 'coffee', 'water']
            return recipe

        elif drink == "white":#2
            recipe = ['cup', 'coffee', 'creamer', 'water']
            return recipe

        elif drink == "sweet":#3
            recipe = ['cup', 'coffee', 'sugar', 'water']
            return recipe

        elif drink == "white and sweet":#4
            recipe = ['cup','coffee', 'sugar', 'creamer', 'water']
            return recipe
 
        elif drink == "bouillon":#5
            recipe = ['cup', 'bouillonPowder', 'water'] 
            return recipe



def main():
    """
    Runs the class coffee machine until user enters quit.
    """

    m = CoffeeMachine(0, 0, 1, 'black')
    while m.one_action():
        pass
    total = m.totalCash()
    print(f'Total cash: ${total/100:.2f}')

if __name__ == "__main__":
    main()