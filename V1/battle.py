import tkinter
from game_window import main_window
from keys import list_of_keys
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


def draw_icons() -> None:
    pc_icon = main_window.battle_canvas.create_rectangle(pc_icon_x, pc_icon_y, pc_icon_x1, pc_icon_y1, fill = 'yellow', outline='black')
    enemy_icon = main_window.battle_canvas.create_rectangle(enemy_icon_x, enemy_icon_y, enemy_icon_x1, enemy_icon_y1,  fill = 'red', outline='black')

def draw_hp_bars() -> None:
    pc_hp_bar_bg = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_hp_x1, pc_hp_y1, fill = 'red', outline='black')
    enemy_hp_bar_bg = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_hp_x1, enemy_hp_y1, fill = 'red', outline='black')
    

    pc_hp_bar_front = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_hp_x1, pc_hp_y1, fill = 'green', outline='black', tags='pc_bar')
    enemy_hp_bar_front = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_hp_x1, enemy_hp_y1, fill = 'green', outline='black', tags='enemy_bar')

def exit_battle():
    if list_of_keys['m']:
        game_state.change_to_map()

def battle_action():
    if list_of_keys['t']:
        game_objects.pc.make_attack(game_objects.goblin)
        
    if list_of_keys['y']:
        game_objects.pc.heal(game_objects.goblin)

    d_hp1 = game_objects.pc.hp/game_objects.pc.max_hp
    d_hp2 = game_objects.goblin.hp/game_objects.goblin.max_hp
    print(d_hp1, d_hp2)


def refresh_hp_bars(d_hp1, d_hp2):
        main_window.battle_canvas.delete('pc_bar')
        main_window.battle_canvas.delete('enemy_bar')

        pc_din_x = pc_hp_x+hp_bar_width*d_hp1
        enemy_din_x = enemy_hp_x+hp_bar_width*d_hp2
        pc_hp_bar_front = main_window.battle_canvas.create_rectangle(pc_hp_x, pc_hp_y, pc_din_x, pc_hp_y1, fill = 'green', outline='black', tags='pc_bar')
        enemy_hp_bar_front = main_window.battle_canvas.create_rectangle(enemy_hp_x, enemy_hp_y, enemy_din_x, enemy_hp_y1, fill = 'green', outline='black', tags='enemy_bar')