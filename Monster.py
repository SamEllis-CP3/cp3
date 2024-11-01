class Monster:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
    
    def Info(self):
        return f"=================\n Name: {self.name}\n From: {self.loc}\n Fighting: {self.attack}\n================="

class Mummy(Monster):
    def __init__(self, name, loc):
        super().__init__(name, loc)
        self.attack = f"{self.name} Wraps his opponet in paper, sffcating them, dealing 25 damage"
        self.Hp = 100

class Dino(Monster):
    def __init__(self, name, loc):
        super().__init__(name, loc)
        self.attack = f"{self.name} bites his opponet dealing 50 damage"
        self.Hp = 100

class Vampire(Monster):
    def __init__(self, name,  loc):
        super().__init__(name, loc)
        self.attack = f"{self.name} sucks the opponets blood out, dealing 30 damage"
        self.Hp = 100

class Ghost(Monster):
    def __init__(self, name, loc):
        super().__init__(name, loc)
        self.attack = f"{self.name} freezes their opponet, dealing 10 damage"
        self.Hp = 100

        

t_rex = Dino("Ethan", "New York")
mum = Mummy("John",  "Egipyt")
vamp = Vampire("Edward","Forks")
app = Ghost("Jarrod", "My closet")

print(t_rex.Info())
print(mum.Info())
print(vamp.Info())
print(app.Info())
