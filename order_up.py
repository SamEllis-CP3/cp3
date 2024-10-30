class Dinner:
    prices = {
        "Drinks": {"Water": 0.00, "Choco Milk": 2.50, "Milk": 3.00, "Coffee": 3.00, "Lemonade": 5.00, "": 2.50, "Hot Chocolate": 3.00, "Soda": 3.00},
        "Appetizers": {"Fries": 4.50, "Bacon wrapped Peppers": 5.00, "Potato wedges": 3.00, "Popcorn Shrimp": 4.00, "Wings": 4.50, "Deep fried Veggies": 3.50, "Load potato": 5.00},
        "Main Courses": {"Steak": 15.00, "Chicken pasta": 13.00, "Burger": 12.50, "Bacon Burger": 14.00, "Burrito": 16.00, "Loaded Nachoes": 10.00, "Chiken sandwitch": 18.00, "Fried fish": 13.50, "Salmon": 12.00},
        "Sides": {"Salad": 2.00, "Baked potato": 2.50, "Butterd corn": 2.00, "Mashed potatoes": 2.50, "Stemed veggies": 2.50, "Texas chili": 3.00, "apple sauce": 1.50},
        "Desserts": {"Apple pie": 4.00, "strawberry cheesecake": 4.50, "big ol brownie": 4.00, "Lava Cake": 5.00, "Cinnabon Mini Swirls": 4.50}
    }

    def __init__(self, drink="", appetizer="", main="", side1="", side2="", dessert=""):
        self.drink = drink
        self.appetizer = appetizer
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

    def __str__(self):
        return (f"Drink: {self.drink}\n"
                f"Appetizer: {self.appetizer}\n"
                f"Main Course: {self.main}\n"
                f"Side 1: {self.side1}\n"
                f"Side 2: {self.side2}\n"
                f"Dessert: {self.dessert}")

    @staticmethod
    def calculate_total(drink, appetizer, main, side1, side2, dessert):
        total = 0
        if drink in Dinner.prices["Drinks"]:
            total += Dinner.prices["Drinks"][drink]
        if appetizer in Dinner.prices["Appetizers"]:
            total += Dinner.prices["Appetizers"][appetizer]
        if main in Dinner.prices["Main Courses"]:
            total += Dinner.prices["Main Courses"][main]
        if side1 in Dinner.prices["Sides"]:
            total += Dinner.prices["Sides"][side1]
        if side2 in Dinner.prices["Sides"]:
            total += Dinner.prices["Sides"][side2]
        if dessert in Dinner.prices["Desserts"]:
            total += Dinner.prices["Desserts"][dessert]
        return total

    def display_menu(self):
        print("\n=== This is our menu of the day! You can choose a drink, an appetizer, a main course, two sides, and a dessert. ===")
        print("1. Drinks")
        print("2. Appetizers")
        print("3. Main Courses")
        print("4. Sides")
        print("5. Desserts")
        print("6. Exit and order.")
        print("*************************")

    def get_choice(self, category, menu):
        print(f"\n{category} Menu:")
        for i, item in enumerate(menu[category], 1):
            print(f"{i}. {item}")
        
        while True:
            try:
                choice = int(input(f"Please select a {category.lower()[:-1]} by typing its number: "))
                if 1 <= choice <= len(menu[category]):
                    selected_item = menu[category][choice - 1]
                    print(f"Got it! You selected {selected_item}.")
                    return selected_item
                else:
                    print(f"Invalid selection. Please choose a number between 1 and {len(menu[category])}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self, menu):
        while True:
            self.display_menu()
            choice = input("Please select what category you want to see (1-6): ")

            if choice == '1':
                self.drink = self.get_choice("Drinks", menu)
            elif choice == '2':
                self.appetizer = self.get_choice("Appetizers", menu)
            elif choice == '3':
                self.main = self.get_choice("Main Courses", menu)
            elif choice == '4':
                print("\nSides:")
                print(", ".join(menu["Sides"]))
                self.side1 = self.get_choice("Sides", menu)
                if self.side1:
                    self.side2 = self.get_choice("Sides", menu)
            elif choice == '5':
                self.dessert = self.get_choice("Desserts", menu)
            elif choice == '6':
                print("\nExiting the program.")
                break
            else:
                print("\nInvalid choice. Please try again.")

        print("\nYour dinner order:")
        print(self)

        # Calculate the total cost
        total_price = Dinner.calculate_total(self.drink, self.appetizer, self.main, self.side1, self.side2, self.dessert)
        print(f"Total Price: ${total_price:.2f}")

menu = {"Drinks": ["Water","Choco Milk","Milk","Coffee","Lemonade","Hot Chocolate","Soda"],
"Appetizers": ["Fries","Bacon wrapped Peppers","Potato wedges","Popcorn Shrimp","Wings","Deep fried Veggies","Loaded potato"],
"Main Courses": ["Steak","Chicken pasta","Burger","Bacon Burger","Burrito","Loaded Nachos","Chicken sandwich","Fried fish","Salmon"],
"Sides": ["Salad","Baked potato","Buttered corn","Mashed potatoes","Steamed veggies","Texas chili","Apple sauce"],
"Desserts": ["Apple pie","Strawberry cheesecake","Big ol brownie","Lava Cake","Cinnabon Mini Swirls"]
}

dinner1 = Dinner()
dinner1.run(menu)