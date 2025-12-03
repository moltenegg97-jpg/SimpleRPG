import tkinter
from game_window import main_window

class GameState:
    def __init__(self, map_frame, battle_frame):
        self.map_frame = map_frame
        self.battle_frame = battle_frame
        self.state = {
            'map': False,
            'battle': False
        }
    def change_to_battle(self):
        self.map_frame.pack_forget()
        self.battle_frame.pack()
        for i in self.state:
            self.state[i] = False
        self.state['battle'] = True
    
    def change_to_map(self):
        self.battle_frame.pack_forget()
        self.map_frame.pack()
        for i in self.state:
            self.state[i] = False
        self.state['map'] = True

game_state = GameState(map_frame=main_window.map_frame, battle_frame=main_window.battle_frame)

