
class Character:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.list_of_actions = ['attack', 'heal']
        self.conditions = {'defending':0}
        self.phy_res = 0
    def make_attack(self, target):
        target.hp = target.hp - self.atk*(1-target.phy_res)
        if target.hp < 0:
            target.hp = 0

    def heal(self, target): #for test
        target.hp = target.hp + self.atk
        if target.hp > target.max_hp:
            target.hp = target.max_hp
    
    def defend(self):
        self.conditions['defending'] = 1
    
    def apply_condition_start_turn(self):
        if self.conditions['defending'] == 0:
            self.phy_res = 0
    def apply_condition_end_turn(self):
        if self.conditions['defending'] > 0:
            self.phy_res = 1

class Goblin(Character):
    def __init__(self, id, **kwargs):
        default_stats = {'hp':100, 'atk':10}
        stats = {**default_stats, **kwargs}
        super().__init__(name='goblin', **stats)
        self.id = id
        self.list_of_actions = ['attack']

class PlayerCharacter(Character):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

character_classes = {'Goblin':Goblin}

enemy_dict = {}

def spawn_enemy(type:str, object_id, **kwargs):
    return character_classes.get(type)(id=object_id, **kwargs)




pc = PlayerCharacter('pc', hp=80, atk=15)
goblin1 = Goblin('1')


if __name__ == '__main__':
    print(goblin1.hp)
    print(goblin1.atk)