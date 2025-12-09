import tkinter
from game_window import main_window
import keys
from game_state_control import game_state
import game_objects
#icons
icon_hight = 100
icon_width = 80

pc_icon_x = 50
pc_icon_y = 50
pc_icon_x1 = pc_icon_x + icon_width
pc_icon_y1 = pc_icon_y + icon_hight

enemy_icon_x = 200
enemy_icon_y = pc_icon_y
enemy_icon_x1 = enemy_icon_x + icon_width
enemy_icon_y1 = enemy_icon_y + icon_hight

#Hp bars
hp_bar_width = icon_width-10
hp_bar_hight = 10

pc_hp_x = pc_icon_x + 5
pc_hp_y = pc_icon_y + icon_hight + 20
pc_hp_x1 = pc_hp_x + hp_bar_width
pc_hp_y1 = pc_hp_y + hp_bar_hight

enemy_hp_x = enemy_icon_x + 5
enemy_hp_y = enemy_icon_y + icon_hight + 20
enemy_hp_x1 = enemy_hp_x + hp_bar_width
enemy_hp_y1 = enemy_hp_y + hp_bar_hight

#значения здоровья
hp_bar_text1_x = pc_hp_x + hp_bar_width/2
hp_bar_text1_y = pc_hp_y - 10
hp_bar_text2_x = enemy_hp_x + hp_bar_width/2
hp_bar_text2_y = enemy_hp_y - 10

hp_bar_textwid1 = main_window.battle_canvas.create_text( hp_bar_text1_x, hp_bar_text1_y, text='')
hp_bar_textwid2 = main_window.battle_canvas.create_text(hp_bar_text2_x, hp_bar_text2_y, text='')

#курсор
cursor_x = 30
cursor_y = 30
cursor_diam = 5
cursor = main_window.battle_canvas.create_oval(cursor_x, cursor_y, cursor_x+cursor_diam, cursor_y+cursor_diam, fill = 'black', outline='black', tags='cursor')

def update_hp_text():
    hp_bar_text1 = f'{game_objects.pc.hp}/{game_objects.pc.max_hp}'
    main_window.battle_canvas.itemconfig(hp_bar_textwid1, text = hp_bar_text1)
    hp_bar_text2 = f'{game_state.enemy_id.hp}/{game_state.enemy_id.max_hp}'
    main_window.battle_canvas.itemconfig(hp_bar_textwid2, text = hp_bar_text2)

def draw_icons() -> None:
    pc_icon = main_window.battle_canvas.create_rectangle(pc_icon_x, pc_icon_y, pc_icon_x1, pc_icon_y1, fill = 'yellow', outline='black')
    enemy_icon = main_window.battle_canvas.create_rectangle(enemy_icon_x, enemy_icon_y, enemy_icon_x1, enemy_icon_y1,  fill = 'red', outline='black')

def draw_hp_bars() -> None:
    pc_hp_bar_bg = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_hp_x1, pc_hp_y1, fill = 'red', outline='black')
    enemy_hp_bar_bg = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_hp_x1, enemy_hp_y1, fill = 'red', outline='black')
    

    pc_hp_bar_front = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_hp_x1, pc_hp_y1, fill = 'green', outline='black', tags='pc_bar')
    enemy_hp_bar_front = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_hp_x1, enemy_hp_y1, fill = 'green', outline='black', tags='enemy_bar')
    update_hp_text()
    
class BattleChoice:
    def __init__(self, name, x:int, y:int):
        self.start_x = 30
        self.start_y = 200
        self.jump_x = 80
        self.jump_y = 30
        self.x_width = 60
        self.y_hight = 15
        self.text_width = 40
        self.text_buf = 5

        self.name = name
        self.x = x
        self.y = y
        main_window.battle_canvas.create_rectangle(self.start_x+self.jump_x*x, self.start_y+self.jump_y*y, self.start_x+self.jump_x*x+self.x_width, self.start_y+self.jump_y*y+self.y_hight, fill = 'white', outline='black')
        main_window.battle_canvas.create_text(self.start_x+self.jump_x*x+self.text_buf, self.start_y+self.jump_y*y, text=self.name, width=self.text_width, anchor='nw')

def draw_battle_options():
    atk_btn = BattleChoice('attack', 0, 0,)
    hl_btn = BattleChoice('heal', 0, 1)
    some_sht = BattleChoice('sm_sht', 1, 0)



def exit_battle():
    if keys.list_of_keys['m']:
        game_state.change_to_map()
    if game_objects.pc.hp <= 0 or game_state.enemy_id.hp <= 0:
         game_state.change_to_map()

def battle_action():
    if keys.list_of_keys['t'] and keys.key_tapped['t']:
            game_objects.pc.make_attack(game_state.enemy_id)
            keys.reset_input_flags()
            
        
    if keys.list_of_keys['y']:
        game_objects.pc.heal(game_state.enemy_id)

    d_hp1 = game_objects.pc.hp/game_objects.pc.max_hp
    d_hp2 = game_state.enemy_id.hp/game_state.enemy_id.max_hp
    refresh_hp_bars(d_hp1, d_hp2)
    update_hp_text()


def refresh_hp_bars(d_hp1, d_hp2):
        main_window.battle_canvas.delete('pc_bar')
        main_window.battle_canvas.delete('enemy_bar')

        pc_din_x = pc_hp_x+hp_bar_width*d_hp1
        enemy_din_x = enemy_hp_x+hp_bar_width*d_hp2
        pc_hp_bar_front = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_din_x, pc_hp_y1, fill = 'green', outline='black', tags='pc_bar')
        enemy_hp_bar_front = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_din_x, enemy_hp_y1, fill = 'green', outline='black', tags='enemy_bar')
        