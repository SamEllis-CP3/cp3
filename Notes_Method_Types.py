import random
class pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl
    def __str__(self) :
        return(f"Name: {self.name}\nType: {self.typ}\nLevel: {self.lvl}\nHp: {self.hp}\n")
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} Won! Hoorray"
        elif self.lvl < other.lvl:
            return f"{other.name} Has defeated you! hoorray"
        else:
            return f"{self.name} and {other.name} are to exhausted to fight. You both lose!"
     #@classmethod used to keep method from chaning object instances!   
    
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp * 1.1)
        return self.lvl
    @classmethod
    def pikachu(self):
        return pokemon(input("Give me a name: "), 50, "Electric", 1)
            
    #static methods do not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5


eevee = pokemon("JayRod", 37, "normal", random.randint(0,20))
charizard = pokemon("bob", 1, "Fire", random.randint(0,20))


pika = pokemon.pikachu()

pika.hp = pokemon.hp_update(pika)
print(eevee.combat(charizard))
print(pika)