class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk

    def make_attack(self, target):
        target.hp = target.hp - self.atk
        if target.hp < 0:
            target.hp = 0

    def heal(self, target): #for test
        target.hp = target.hp + self.atk
        if target.hp > target.max_hp:
            target.hp = target.max_hp
        

pc = Character('pc', hp=80, atk=5)
goblin = Character('goblin', hp=100, atk=10)
