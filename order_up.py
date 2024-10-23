class Order:
    def __init__(self):
        self.total = 0.0
        self.finalorder = []
        

    

        
        
        
    def DrinkOrder(self):
        D_Choice = input(f"What would you like to order?\n{drinklst}\n:")
        while True:
            
            
            if D_Choice.lower == "water":
                self.finalorder.append("Water")
                more = input("Would you like to order anything else?\n:")
                if more.lower == "yes":
                    pass
                elif more.lower == "no":
                    break

            elif D_Choice.lower == "orange juice":
                self.finalorder.append("Orange Juice")
                self.total += 1.50
                more = input("Would you like to order anything else?\n:")
                if more.lower == "yes":
                    pass
                elif more.lower == "no":
                    break

            elif D_Choice.lower == "apple juice":
                self.finalorder.append("Apple Juice")
                self.total += 1.50
                more = input("Would you like to order anything else?\n:")
                if more.lower == "yes":
                    pass
                elif more.lower == "no":
                    break

            elif D_Choice.lower == "coffe":
                self.finalorder.append("Coffe")
                self.total += 3.00
                more = input("Would you like to order anything else?\n:")
                if more.lower == "yes":
                    pass
                elif more.lower == "no":
                    break
            elif D_Choice.lower == "hot chocolate":
                self.finalorder.append("Hot Chocolate")
                self.total += 1.50
                more = input("Would you like to order anything else?\n:")
                if more.lower == "yes":
                    pass
                elif more.lower == "no":
                    break
            else:
                print('Ok')
                break
        print(self.finalorder)
        print(self.total)
        
        




drinklst = [ 'Water: Free', "Orange Juice: $1.50", "Apple Juice: $1.50", "Coffe: $3.00", "Hot Chocolate: $1.50", "Nothing"]
applst = ["Chips n Salsa: $5.00","Guacamole: $5.00", "Jalapeno Poppers: $4.50" ]
sidelst = ["Potato Skins: $3.50", "Mashed potatos: $3.50","Fries: $3.50"]
desslst = ["Choco Cake: $5.00", "Lava Cake: $5.00", "Choco Icecream: $3.50"]
menu = (f"\nDrinks {drinklst}\nAppetizers {applst}\nSides {sidelst}\n Desserts {desslst}")

Order.DrinkOrder()