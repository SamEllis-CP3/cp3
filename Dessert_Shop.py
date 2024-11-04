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

class Order:
    def __init__(self):
        self.order = []

    def add(self, item):
        self.item = item
        
        self.order.append(self.item)
        

    def __len__(self):
        size = len(self.order)
        return size

def main():
    Order_1 = Order()
    
    Order_1.add(Candy("Candy Corn", 1.5, .25))
    Order_1.add(Candy("Gummy Bears", .25, .35))
    Order_1.add(Cookie("Chocolate Chip", 6, 3.99))
    Order_1.add(IceCream("Pistachio", 2, .79))
    Order_1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order_1.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in Order_1.order:
        print(item)
    print(f"Total number of items in order: {len(Order_1)}")
    
    

main()