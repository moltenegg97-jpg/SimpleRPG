from game_window import main_window
import inventory

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
        damage_done = self.atk*(1-target.phy_res)
        target.hp = target.hp - damage_done
        if target.hp < 0:
            target.hp = 0
        main_window.add_battle_log(f'{self.name,} attacks')
        main_window.add_battle_log(f'its done {damage_done} damage')
    def heal(self, target): #for test
        target.hp = target.hp + self.atk
        if target.hp > target.max_hp:
            target.hp = target.max_hp
        main_window.add_battle_log(f'{self.name,} heals')
        main_window.add_battle_log(f'its heals {self.atk}')
    def defend(self):
        self.conditions['defending'] = 1
        main_window.add_battle_log(f'{self.name,} is defending')
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
item_dict = {}

def spawn_enemy(type:str, object_id, **kwargs):
    return character_classes.get(type)(id=object_id, **kwargs)

class Item:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.sprite = None
        self.sprite_size = 5
        self.sprite_color = 'orange'
        self.heal_power = 15
    def spawn(self, x, y):
        self.sprite = main_window.map_canvas.create_rectangle(x, y, x+self.sprite_size, y+self.sprite_size, fill=self.sprite_color, outline='black', tags='item')
        item_dict[self.sprite] = self
        print(self.sprite)
    def pick_up(self):
        print(self.sprite, self.sprite_size)
        inventory_size = self.sprite_size * 3
        border = 8
    
        for i in range(len(inventory.layout)):
            for j in range(len(inventory.layout[i])):
                if inventory.layout[i][j] == 0:
                    inventory.layout[i][j] = self.sprite
                    x = border+j*inventory.tile_size
                    y = border+i*inventory.tile_size
                    x1 = x+inventory_size
                    y1 = y+inventory_size
                    self.inventory_sprite = main_window.inventory_canvas.create_rectangle(x, y, x1, y1, fill=self.sprite_color, outline="black")
                    return
    def drink(self):
        hp_before = pc.hp
        pc.hp = min(pc.hp+self.heal_power, pc.max_hp)
        d_hp = pc.hp - hp_before
        main_window.inventory_canvas.delete(self.inventory_sprite)
        main_window.add_battle_log(f'{pc.name} использовал {self.name} и вылечил {d_hp}')


pc = PlayerCharacter('pc', hp=80, atk=15)
goblin1 = Goblin('1')
potion1 = Item('potion', 1)
potion2 = Item('potion', 2)

if __name__ == '__main__':
    print(goblin1.hp)
    print(goblin1.atk)