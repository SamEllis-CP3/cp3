class DessertItem:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    
class Candy(DessertItem):
    def __init__(self, name,candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    
    def get_cost(self):
        return self.price_per_pound
    
    def get_weight(self):
        return self.candy_weight
    

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def get_cost(self):
        return self.price_per_dozen
    
    def get_amount(self):
        return self.quantity
    
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def get_scoop(self):
        return self.scoop_count
    
    def get_cost(self):
        return self.price_per_scoop

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_topping(self):
        return self.topping_name
    
    def get_topping_price(self):
        return self.topping_price
    