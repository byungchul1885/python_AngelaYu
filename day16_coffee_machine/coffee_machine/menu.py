from menu_item import MenuItem

class Menu:
    item = {}
    def __init__(self):
        self.item["espresso"] = MenuItem("espresso", 1.5,
                                         {"water": 50,"coffee": 18})
        self.item["latte"] = MenuItem("latte", 2.5,
                                         {"water": 200,"milk": 150,
                                          "coffee": 24})
        self.item["cappuccino"] = MenuItem("cappuccino", 3.0,
                                         {"water": 250,"milk": 100,
                                          "coffee": 24})        
    def get_items(self):
        r = ""
        for m in self.item:
            r += m + "/"
        r = r.rstrip('/')
        return r
    
    def find_drink(self, order_name):
        for m in self.item:
            if order_name == m:
                return self.item[m]
        return None