import random



class Character:
    def __init__(self, name, Hp, Atc):
        self.name = name
        self.Hp = Hp
        self.Atc = Atc
        self.isDefending = False
        self.HpMax = Hp
    

    def make_attack(self, target):
        if target.isDefending == False:
            target.Hp = target.Hp - self.Atc
            target.isDefending = False
        if target.isDefending == True:
            target.isDefending = False

    def defend(self):
        self.isDefending = True

PC = Character('PC', Hp=100, Atc=15)
Goblin = Character('Goblin', Hp=60, Atc=5)

def battle_cicle():
    
    while Goblin.Hp > 0 and PC.Hp > 0:
        player_input = input('введите a для атаки d  для защиты :')
        if player_input == 'a':
            print('PC атакует')
            PC.make_attack(Goblin)
        if player_input == 'd':
            print('PC защищается')
            PC.defend()
            print (PC.name, PC.Hp)
            print (Goblin.name, Goblin.Hp)

        goblin_choice = random.randint(1, 2)
        if goblin_choice == 1:
            print('Goblin атакует')
            Goblin.make_attack(PC)
        if goblin_choice == 2:
            print('Goblin защищается')
            Goblin.defend()
        print (PC.name, PC.Hp)
        print (Goblin.name, Goblin.Hp)
        
        if Goblin.Hp <= 0 or PC.Hp <= 0:
            return True
        
if __name__ == '__main__':

    print (PC.name, PC.Hp)
    print (Goblin.name, Goblin.Hp)

    battle_cicle()

    