from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25
    def get_name(self):
        return self.name
    
    @abstractmethod
    def calc_cost(self):
        pass
        
    
    
class Candy(DessertItem):
    def __init__(self, name,candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    
    def get_cost(self):
        return self.price_per_pound
    
    def get_weight(self):
        return self.candy_weight
    
    def calc_cost(self):
        base_cost = self.candy_weight * self.price_per_pound
        total_cost = base_cost * (1 + base_cost * self.tax_percent)
        return total_cost

class Cookie(DessertItem):
    def __init__(self, name, quantity, price_per_dozen):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

    def get_cost(self):
        return self.price_per_dozen
    
    def get_amount(self):
        return self.quantity
    
    def calc_cost(self):
        base_cost = (self.quantity / 12) * (self.price_per_dozen)
        total_cost = base_cost * (1 + base_cost * self.tax_percent)
        return total_cost
    
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def get_scoop(self):
        return self.scoop_count
    
    def get_cost(self):
        return self.price_per_scoop
    
    def calc_cost(self):
        base_cost = self.price_per_scoop * self.scoop_count
        total_cost = base_cost * (1 + base_cost * self.tax_percent)
        return total_cost

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_topping(self):
        return self.topping_name
    
    def get_topping_price(self):
        return self.topping_price
    
    def calc_cost(self):
        ice_cream_cost = self.scoop_count * self.price_per_scoop
        total_cost = ice_cream_cost + self.topping_price
        total_cost_with_tax = total_cost * (1 + total_cost * self.tax_percent / 100)
        return total_cost_with_tax

class Order:
    def __init__(self):
        self.order = []

    def add(self, item):
        self.item = item
        
        self.order.append(self.item)
        

    def __len__(self):
        size = len(self.order)
        return size
    
    def order_cost(self):
        return sum(item.calc_cost() for item in self.order)
    
    def order_tax(self):
        total_tax = 0
        for item in self.order:
            base_cost = item.calc_cost() / (1 + item.tax_percent / 100)
            total_tax += item.calc_cost() - base_cost
        return total_tax
    
list_items = []

def main():
    Order_1 = Order()
    
    Order_1.add(Candy("Candy Corn", 1.5, .25))
    Order_1.add(Candy("Gummy Bears", .25, .35))
    Order_1.add(Cookie("Chocolate Chip", 6, 3.99))
    Order_1.add(IceCream("Pistachio", 2, .79))
    Order_1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order_1.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in Order_1.order:
        print(f"{item.get_name()} - ${item.calc_cost():.2f}")
        list_items.append(f"{item.get_name()} - ${item.calc_cost():.2f}")

    print(f"Total number of items in order: {len(Order_1)}")
    
    print(f"Total cost of the order: ${Order_1.order_cost():.2f}")
    print(f"Total tax applied: ${Order_1.order_tax():.2f}")
    
    

main()








# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
  
# data which we are going to display as tables 
DATA = [ 
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
    [ 
        "16/11/2020", 
        "Full Stack Development with React & Node JS - Live", 
        "Lifetime", 
        "10,999.00/-", 
    ], 
    [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
    [ "Sub Total", "", "", "20,9998.00/-"], 
    [ "Discount", "", "", "-3,000.00/-"], 
    [ "Total", "", "", "17,998.00/-"], 
] 
  
# creating a Base Document Template of page size A4 
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 
  
# standard stylesheet defined within reportlab itself 
styles = getSampleStyleSheet() 
  
# fetching the style of Top level heading (Heading1) 
title_style = styles[ "Heading1" ] 
  
# 0: left, 1: center, 2: right 
title_style.alignment = 1
  
# creating the paragraph with  
# the heading text and passing the styles of it 
title = Paragraph( "GeeksforGeeks" , title_style ) 
  
# creates a Table Style object and in it, 
# defines the styles row wise 
# the tuples which look like coordinates  
# are nothing but rows and columns 
style = TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
) 
  
# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 
  
# final step which builds the 
# actual pdf putting together all the elements 
pdf.build([ title , table ]) 