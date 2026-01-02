import tkinter
from game_window import main_window


class GameState:
    
    def __init__(self, map_frame, battle_frame, inventory_frame):
        self.map_frame = map_frame
        self.battle_frame = battle_frame
        self.inventory_frame = inventory_frame
        self.corrent_state = None
        self.previous_state = None
        self.state = {
            'map': False,
            'battle': False,
            'inventory':False
        }
        self.enemy_id = None #объект с которым идёт бой      
    def change_to_battle(self, id):
        self.map_frame.pack_forget()
        self.inventory_frame.pack_forget()
        self.battle_frame.pack()
        self.enemy_id = id
        for i in self.state:
            self.state[i] = False
        self.state['battle'] = True
        self.corrent_state = 'battle'

    def change_to_inventory(self):
        self.previous_state = self.corrent_state
        if self.previous_state == 'battle':
            self.battle_frame.pack_forget()
        if self.previous_state == 'map':
            self.map_frame.pack_forget()
        self.inventory_frame.pack()
        for i in self.state:
            self.state[i] = False
        self.state['inventory'] = True
        self.corrent_state = 'inventory'

    def back_from_inventory(self):
        if self.previous_state == 'battle':
            self.change_to_battle(self.enemy_id)
        if self.previous_state == 'map':
            self.change_to_map()

    def change_to_map(self):
        self.battle_frame.pack_forget()
        self.inventory_frame.pack_forget()
        self.map_frame.pack()
        for i in self.state:
            self.state[i] = False
        self.state['map'] = True
        self.corrent_state = 'map'

game_state = GameState(map_frame=main_window.map_frame, battle_frame=main_window.battle_frame, inventory_frame=main_window.inventory_frame)

