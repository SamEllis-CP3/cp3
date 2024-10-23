#We start classes with keyword class and we name them using PascalCase
class animal:
    #we start with the constuctor (Defines all of the attributes of the object being created)
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
    #Methods are dunctions inside of the class
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) == len(other.name):
            self.losses += 1
            other.losses += 1
            return "Tie"
        else:
            self.losses += 1
            return other.name
    
    #Makes a more readable string when printed
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}\n"
    def get_name(self):
        return self.name
    
#We generaly store objects in variables (individually or in a list) so we can use it!
cat = animal("Tom", "cat", 21, "Male", "Common")
frog = animal("Jarrod", "Posion dart frog", 500, "Female", "Rare")

cat.losses = 0
frog.losses = 0

#To call a method you put a name of a object.name of the method(Needed arguements)
print(cat.fight(frog))

cat.losses = 1

cat.name = "Thomas"

print(cat.losses)

print(cat.fight(frog))

print(cat.losses)
print(frog.losses)

print(f"Your pet {cat.name} died")
cat = None
