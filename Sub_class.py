class PetStore:
    name = "Pet Smart"
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        self.featured_pet = None

    def add_pet(self, animal):
        assert isinstance(animal, Animal)
        self.animals.append(animal)

    def remove_pet(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("No such animal")
        else:
            print(animal, "removed")
        
    def feature(self, name):
        for pet in self.animals:
            if pet.name == name:
                self.featured_pet = pet
                print("Featured pet. . .", pet)
                break
        else:
            print("No Such pet exsist")

    def get_featured(self):
        return self.featured_pet
    
    def feed(self):
        for pet in self.animals:
            pet.eat()
        
    def get_mammals(self):
        return self.get_by_type(Mammal)
    
    def get_birds(self):
        return self.get_by_type(Birds)
    
    def get_reptiles(self):
        return self.get_by_type(Reptile)
    
    def get_amphibians(self):
        return self.get_by_type(Amphibians)
    
    def get_fish(self):
        return self.get_by_type(Fish)
    
    def get_by_type(self, typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]
    

class Animal:

    def __init__(self, name):
        self.name = name
    

    def __str__(self):
        return f"This is {self.name}"
    
    def eat(self):
        print(f"{self.name} eating {self.diet}")

class Mammal(Animal):
    pass

class Cat(Mammal):
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"

class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodents"

class Turtle(Reptile):
    diet = "carrots"

class Bird():
    pass

class Pigeon(Bird):
    diet = "New yorkers"
class Tucan(Bird):
    diet = "fuit loops"


class Amphibians():
    pass
class Frog(Amphibians):
    diet = "flies"
class Newt(Amphibians):
    diet = "worms"

class Fish():
    pass
class Koi(Fish):
    diet = "algae"
class Guppy(Fish):
    diet = "flakes"

store = PetStore(1)
store.add_pet(Turtle("Shelly"))
store.add_pet(Cat("Joe"))
store.add_pet(Turtle("Flash"))
store.add_pet(Bird("Robin"))

store.feature("Flash")
store.feed()

print("\nReptiles: ")
for pet in store.get_reptiles():
    print(pet)
