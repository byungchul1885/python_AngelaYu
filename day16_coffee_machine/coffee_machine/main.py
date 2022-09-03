from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

off_machine = False
while not off_machine:
    order = input(f"What would you like? ({menu.get_items()}): ")
    order = order.lower()

    if order == "off":
        off_machine = True
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(order)
        if menu_item == None:
            print(f"This machine has no {order} menu")
            continue
            
        if not coffee_maker.is_resource_sufficient(menu_item):
            continue
        
        recv_money = money_machine.get_money()
        
        if money_machine.isPaymentOk(recv_money, menu_item.costs):
            coffee_maker.make_coffee(menu_item)      
            print(f"Here is your {order}. Enjoy!.")

