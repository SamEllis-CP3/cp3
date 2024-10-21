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
        
        sp = ":"
        finalorder = []
        total = 0.00
        drinkT = True
        print("Would you like to order a drink?")
        drinktof = input(":")
        if drinktof.lower == "yes":
            while drinkT:
            
                drinkch = input(f"What drink would you like{drinklst}\n:")
                if drinkch.lower == "water":
                    total += 0
                    print(f"You order {drinkch}")
                    finalorder.append(drinkch)
                    wld = input('Would you like to order another drink?\n:')
                    if wld == "no" or wld == "No":
                        drinkT = False
                    elif wld == "Yes" or wld == "yes":
                        print("\n")

                elif drinkch == "orange juice":
                    total += 1.50
                    print(f"You order {drinkch}")
                    finalorder.append(drinkch)
                    wld = input('Would you like to order another drink?\n:')
                    if wld.lower == "no":
                        drinkT = False
                    elif wld == "yes":
                        print("\n")

                elif drinkch == "apple juice":
                    total += 1.50
                    print(f"You order {drinkch}")
                    finalorder.append(drinkch)
                    wld = input('Would you like to order another drink?\n:')
                    if wld.lower == "no":
                        drinkT = False
                    elif wld == "yes":
                        print("\n")

                elif drinkch == "coffe":
                    total += 3.00
                    print(f"You order {drinkch}")
                    finalorder.append(drinkch)
                    wld = input('Would you like to order another drink?\n:')
                    if wld.lower == "no":
                        drinkT = False
                    elif wld == "yes":
                        print("\n")

                elif drinkch == "nothing":
                    
                    wld = (input('Would you like to order another drink?\n:'))
                    if wld.lower == "no":
                        drinkT = False
                    elif wld == "yes":
                        print("\n")

                else:
                    print("That is not on the menu")
            
        elif drinktof == "no":
            print("\n")


        specialins = input("Do you have any Special instuctions for your drink\n")   
        if specialins  == "Yes" or specialins == "yes":
            specinst = input("What would you like to be done with your drink?")
            sp = sp + specinst
        elif specialins  == "No" or specialins == "no":
            print("\n")
            

        print(f"Your total is ${total}\nYour order is{finalorder}")
        print(sp)
        
        




drinklst = [ 'Water: Free', "Orange Juice: $1.50", "Apple Juice: $1.50", "Coffe: $3.00", "Hot Chocolate: $1.50", "Nothing"]
applst = ["Chips n Salsa: $5.00","Guacamole: $5.00", "Jalapeno Poppers: $4.50" ]
sidelst = ["Potato Skins: $3.50", "Mashed potatos: $3.50","Fries: $3.50"]
desslst = ["Choco Cake: $5.00", "Lava Cake: $5.00", "Choco Icecream: $3.50"]
menu = (f"\nDrinks {drinklst}\nAppetizers {applst}\nSides {sidelst}\n Desserts {desslst}")

Order.orderdone()