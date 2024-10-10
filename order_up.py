class Order:
    def __init__(self, drink, appetizer, side1, side2, dessert, total):
        self.drink = drink
        self.appetizer = appetizer
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
        self.total = total

    

        
        
        
    @staticmethod
    def orderdone():
        finalorder = []
        total = 0
        while True:
            drinkch = input(f"What drink would you like{drinklst}\n:")
            if drinkch == "water" or drinkch == "Water":
                total += 0
                print(f"You order {drinkch}")
                finalorder.append
            elif drinkch == "Orange Juice" or drinkch == "orange juice":
                total += 1.50
                print(f"You order {drinkch}")
            elif drinkch == "Apple Juice" or drinkch == "apple juice":
                total += 1.50
                print(f"You order {drinkch}")
            elif drinkch == "Coffe" or drinkch == "coffe":
                total += 3.00
                print(f"You order {drinkch}")
            else:
                print("Are You sure you would not like a drink?")
                drinktof = input(":")
                if drinktof == "yes" or drinktof == "Yes":
        




drinklst = [ 'Water: Free', "Orange Juice: $1.50", "Apple Juice: $1.50", "Coffe: $3.00", "Hot Chocolate: $1.50", "Nothing"]
applst = ["Chips n Salsa: $5.00","Guacamole: $5.00", "Jalapeno Poppers: $4.50" ]
sidelst = ["Potato Skins: $3.50", "Mashed potatos: $3.50","Fries: $3.50"]
desslst = ["Choco Cake: $5.00", "Lava Cake: $5.00", "Choco Icecream: $3.50"]
menu = (f"\nDrinks {drinklst}\nAppetizers {applst}\nSides {sidelst}\n Desserts {desslst}")

Order.orderdone()