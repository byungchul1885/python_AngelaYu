from menu import MENU

water_remain = 300
milk_remain = 200
coffee_remain = 100
money_earned = 0
off_machine = False

def check_water_remain(order):
    if water_remain < MENU[order]["ingredients"]["water"]:
        return False
    else:
        return True
    
def check_coffee_remain(order):
    if coffee_remain < MENU[order]["ingredients"]["coffee"]:
        return False
    else:
        return True
    
def check_milk_remain(order):
    if 'milk' in MENU[order]["ingredients"].keys():
        if milk_remain < MENU[order]["ingredients"]["milk"]:
            return False
        else:
            return True
    else:
        return True

def report():
    print(f"Water: {water_remain}ml")
    print(f"Milk: {milk_remain}ml")
    print(f"Coffee: {coffee_remain}g")
    print(f"Money: ${money_earned}")
        
def get_money():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    
    return quarters * 0.25 + dimes * 0.1 + \
        nickles * 0.05 + pennies * 0.01
    
while not off_machine:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    order = order.lower()

    if order == "off":
        off_machine = True
    elif order == "report":
        report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if not check_water_remain(order):
            print(f"Sorry there is not enough water.")
            continue
        elif not check_milk_remain(order):
            print(f"Sorry there is not enough milk.")   
            continue
        elif not check_coffee_remain(order):
            print(f"Sorry there is not enough coffee.")           
            continue
        
        print("Please insert coins.")
        
        needed_money = MENU[order]["cost"]
        recv_money = get_money()
        
        if (needed_money > recv_money):
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif (needed_money < recv_money):
            print(f"Here is ${round(recv_money - needed_money, 2)} in change.")
        
        
        water_remain -= MENU[order]["ingredients"]["water"]
        if 'milk' in MENU[order]["ingredients"].keys():
            milk_remain -= MENU[order]["ingredients"]["milk"]
        coffee_remain -= MENU[order]["ingredients"]["coffee"]
        money_earned += MENU[order]["cost"]
        
        print(f"Here is your {order}. Enjoy!.")
            

