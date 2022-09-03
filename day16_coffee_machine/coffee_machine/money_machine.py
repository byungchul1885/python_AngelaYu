class MoneyMachine:
    def __init__(self):
        self.profit = 0
        
    def report(self):
        print(f"Money: ${self.profit}")
        
    def get_money(self ):
        print("Please insert coins.")
        
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        
        return quarters * 0.25 + dimes * 0.1 + \
            nickles * 0.05 + pennies * 0.01
            
    def isPaymentOk(self, recv_money, price):
        if (price > recv_money):
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif (price < recv_money):
            print(f"Here is ${round(recv_money - price, 2)} in change.")
            self.profit += price
            return True
        else:
            self.profit += price
            return True