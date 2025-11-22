class Character:
    def __init__(self, name, Hp, Atc):
        self.name = name
        self.Hp = Hp
        self.Atc = Atc
    

    def make_attack(self, target):
        target.Hp = target.Hp - self.Atc

PC = Character('PC', 100, 15)
Goblin = Character('Goblin', 60, 5)

print (PC.name, PC.Hp)
print (Goblin.name, Goblin.Hp)