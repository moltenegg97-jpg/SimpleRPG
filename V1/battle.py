import tkinter
from game_window import main_window

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

def draw_icons()->None:
    pc_icon = main_window.battle_canvas.create_rectangle(pc_icon_x, pc_icon_y, pc_icon_x1, pc_icon_y1, fill = 'yellow', outline='black')
    enemy_icon = main_window.battle_canvas.create_rectangle(enemy_icon_x, enemy_icon_y, enemy_icon_x1, enemy_icon_y1,  fill = 'red', outline='black')