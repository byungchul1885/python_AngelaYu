from menu_item import MenuItem


class CoffeeMaker:
    
    def __init__(self):
        self.resources = {"water" : 300,
                          "milk" : 200,
                          "coffee" : 100}
        
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        
    def is_resource_sufficient(self, drink: MenuItem):
        igdts = drink.ingredients
        
        for item in igdts:
            if igdts[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")                
                return False
        return True
    
    def make_coffee(self, order: MenuItem):
        igdts = order.ingredients
        
        for item in igdts:
            self.resources[item] -= igdts[item]
    