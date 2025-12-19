import tkinter
from game_window import main_window
import keys
from game_state_control import game_state
import game_objects


battle_option_table = {}

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

class Cursor():
    def __init__(self):
        self.cursor_pos_x = 0
        self.cursor_pos_y = 0
        cursor_x = 95
        cursor_y = 205
        self.cursor_jp_x = 80
        self.cursor_jp_y = 30
        cursor_diam = 5
        self.cursor = main_window.battle_canvas.create_oval(cursor_x, cursor_y, cursor_x+cursor_diam, cursor_y+cursor_diam, fill = 'black', outline='black', tags='cursor')
        self.choice_callback = None

    def set_choice_callback(self, callback):
        self.choice_callback = callback

    def move_cursor(self):
        dx, dy = 0, 0
        if keys.key_tapped['w'] and main_window.battle_canvas.coords(self.cursor)[1] > 205: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_y -= 1
            dy -= self.cursor_jp_y
            keys.reset_input_flags()
        if keys.key_tapped['s'] and main_window.battle_canvas.coords(self.cursor)[1] < 235: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_y += 1
            dy += self.cursor_jp_y
            keys.reset_input_flags()
        if keys.key_tapped['a'] and main_window.battle_canvas.coords(self.cursor)[0] > 95: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_x -= 1
            dx -= self.cursor_jp_x
            keys.reset_input_flags()
        if keys.key_tapped['d'] and main_window.battle_canvas.coords(self.cursor)[0] < 255: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_x +=1
            dx += self.cursor_jp_x
            keys.reset_input_flags()
        if keys.key_tapped['u']:
            print(battle_option_table)
            keys.reset_input_flags()
            #print(battle_canvas.coords(cursor))
        main_window.battle_canvas.move(self.cursor, dx, dy)

    def pick_battle_option(self) -> bool: #if true - turn ended
        if keys.key_tapped['Return']:
            print('key is pressed') #для теста, удалить позже
            print(self.cursor_pos_x, self.cursor_pos_y) #для теста, удалить позже
            print(battle_option_table.get((self.cursor_pos_x, self.cursor_pos_y))) #для теста, удалить позже
            print(main_window.battle_canvas.coords(self.cursor))
            action = battle_option_table.get((self.cursor_pos_x, self.cursor_pos_y))
            if action in ['attack', 'heal', 'defend']:
                if action == 'attack':
                    game_objects.pc.make_attack(game_state.enemy_id)
                elif action == 'heal':
                    game_objects.pc.heal(game_state.enemy_id)
                elif action == 'defend':
                    game_objects.pc.defend()
                keys.reset_input_flags()

                if self.choice_callback:
                    self.choice_callback(action)
                print(game_objects.pc.conditions)
                return True
        return False

cursor = Cursor()

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
        battle_option_table[(x, y)] = name
        self.name = name
        self.x = x
        self.y = y
        main_window.battle_canvas.create_rectangle(self.start_x+self.jump_x*x, self.start_y+self.jump_y*y, self.start_x+self.jump_x*x+self.x_width, self.start_y+self.jump_y*y+self.y_hight, fill = 'white', outline='black')
        main_window.battle_canvas.create_text(self.start_x+self.jump_x*x+self.text_buf, self.start_y+self.jump_y*y, text=self.name, width=self.text_width, anchor='nw')

def draw_battle_options():
    atk_btn = BattleChoice('attack', 0, 0,)
    hl_btn = BattleChoice('heal', 0, 1)
    defend_btn = BattleChoice('defend', 1, 0)


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
        