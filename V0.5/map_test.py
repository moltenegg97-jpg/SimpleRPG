import tkinter
import battle_logic

#матрица карты
map_matrix = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
tile_size = 20
main_window = tkinter.Tk()
map_canvas = tkinter.Canvas(main_window)
map_canvas.pack()

battle_canvas = tkinter.Canvas(main_window)
# map_canvas.create_rectangle(50, 50, 70, 70, fill="blue", outline="black")
# map_canvas.create_rectangle(200, 200, 220, 220, fill="green", outline="black")

#отрисовываю карту
for i in range(len(map_matrix)):
    for j in range(len(map_matrix[i])):
        if map_matrix[i][j] == 1:
            color = 'blue'
            layer = 'wall'
        if map_matrix[i][j] == 0:
            color = 'green'
            layer = 'background'
        map_canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill=color, outline="black", tags=layer)
#отрисовка персонажа
playerY = 30
playerX = 30
character = map_canvas.create_oval(playerY, playerX, playerY+8, playerX+8, fill = 'yellow', outline='black', tags='character')

goblin1 = map_canvas.create_oval(40, 100, 48, 108, fill='red', outline='black', tags='enemy')
goblin2 = map_canvas.create_oval(70, 80, 78, 88, fill='red', outline='black', tags='enemy')

#отрисовка персонажей на экране боя
player_battle_icon_x = 50
player_battle_icon_y = 50
player_battle_icon_width = 80
player_battle_icon_hight = 100

enemy_battle_icon_x = 200
enemy_battle_icon_y = 50
enemy_battle_icon_width = 80
enemy_battle_icon_hight = 100

player_battle_icon = battle_canvas.create_rectangle(player_battle_icon_x, player_battle_icon_y, player_battle_icon_x+player_battle_icon_width, player_battle_icon_y+player_battle_icon_hight, fill = 'yellow', outline='black')
enemy_battle_icon = battle_canvas.create_rectangle(enemy_battle_icon_x, enemy_battle_icon_y, enemy_battle_icon_x+enemy_battle_icon_width, enemy_battle_icon_y+enemy_battle_icon_hight, fill = 'red', outline='black')

#отрисовка полос здоровья
player_battle_hp_x = player_battle_icon_x+10
player_battle_hp_y = player_battle_icon_y+player_battle_icon_hight+20
player_battle_hp_x1 = player_battle_icon_x+player_battle_icon_width-10
player_battle_hp_y1 = player_battle_icon_y+player_battle_icon_hight+20+10
player_battle_hp_x_din = battle_logic.PC.Hp/battle_logic.PC.HpMax

player_battle_hp_bar_back = battle_canvas.create_rectangle(player_battle_hp_x, player_battle_hp_y, player_battle_hp_x1, player_battle_hp_y1, fill = 'red', outline='black')
player_battle_hp_bar_back = battle_canvas.create_rectangle(player_battle_hp_x, player_battle_hp_y, player_battle_hp_x1, player_battle_hp_y1, fill = 'green', outline='black', tags='pc_bar')

enemy_battle_hp_x = enemy_battle_icon_x+10
enemy_battle_hp_y = enemy_battle_icon_y+enemy_battle_icon_hight+20
enemy_battle_hp_x1 = enemy_battle_icon_x+enemy_battle_icon_width-10
enemy_battle_hp_y1 = enemy_battle_icon_y+enemy_battle_icon_hight+20+10
enemy_battle_hp_x_din = battle_logic.Goblin.Hp/battle_logic.Goblin.HpMax

enemy_battle_hp_bar_back = battle_canvas.create_rectangle(enemy_battle_hp_x, enemy_battle_hp_y, enemy_battle_hp_x1, enemy_battle_hp_y1, fill = 'red', outline='black')
enemy_battle_hp_bar_back = battle_canvas.create_rectangle(enemy_battle_hp_x, enemy_battle_hp_y, enemy_battle_hp_x1, enemy_battle_hp_y1, fill = 'green', outline='black', tags='enemy_bar')

class action_text:
    def __init__(self, disposition_x, disposition_y, text):
        self.text_width = 40 
        self.text_x = 50+ disposition_x 
        self.text_y = 200 + disposition_y
        self.text_bar_size = 14
        self.text = text
        battle_canvas.create_rectangle(self.text_x-5, self.text_y, self.text_x+self.text_width+5, self.text_y+self.text_bar_size, fill = 'white', outline='black')
        battle_canvas.create_text(self.text_x, self.text_y, text=self.text, width=self.text_width, anchor='nw')

attack_text = action_text(0, 0, 'attack')
block_text = action_text(0, 30, 'block')


#курсор
cursor_diametr = 5
cursor_x = attack_text.text_x + attack_text.text_width + 10
cursor_y = attack_text.text_y + attack_text.text_bar_size/2 - cursor_diametr/2

cursor = battle_canvas.create_oval(cursor_x, cursor_y, cursor_x+cursor_diametr, cursor_y+cursor_diametr, fill = 'black', outline='black', tags='cursor')

keys_pressed = {
    'w': False,
    'a': False, 
    's': False,
    'd': False,
    'm': False,
    'Return': False
}
game_states = {
    'map': True,
    'battle': False
}


def key_pressed(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True


def key_released(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False

def can_move(list_of_overlaps):
    if 'wall' in list_of_overlaps:
            print('найдено пересечание')
            return False
    if 'enemy' in list_of_overlaps:
            print('найдено пересечание')
            to_battle_state()
            map_canvas.delete(list_of_overlaps['enemy'][0])
            # map_canvas.delete('enemy')
            return False
    return True

def to_battle_state():
    map_canvas.pack_forget()
    battle_canvas.pack()
    game_states['map'] = False
    game_states['battle'] = True
    #main_window.after(16, to_battle_state)
    
    if battle_logic.battle_cicle() == True:
        to_map_state()

def key_for_map_state():
    if keys_pressed['m']:
        to_map_state()
    main_window.after(16, key_for_map_state)

def to_map_state():
    
    battle_canvas.pack_forget()
    map_canvas.pack()
    game_states['battle'] = False
    game_states['map'] = True
        
    

def check_for_overlaps(collision_x1, collision_y1, collision_x2, collision_y2):
    overlaps_id = (map_canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2))
    list_of_overlaps_tags = {}
    print(overlaps_id)
        
    for i in overlaps_id:
            
        #list_of_overlasps_tags.append(map_canvas.gettags(i)[0])
        if map_canvas.gettags(i)[0] in list_of_overlaps_tags:
            print('такой тег был')
            print(list_of_overlaps_tags[map_canvas.gettags(i)[0]])
            list_of_overlaps_tags[map_canvas.gettags(i)[0]].append(i)
        else:
            list_of_overlaps_tags[map_canvas.gettags(i)[0]] = [i]
        
            #print(collision_x1, collision_y1, collision_x2, collision_y2)
            print(map_canvas.bbox(character))
            print(list_of_overlaps_tags)
    return list_of_overlaps_tags
# Функция, которая периодически проверяет состояние клавиш и двигает персонажа
def character_movement():
    
    if game_states['map'] == True:
        dx, dy = 0, 0
    
        if keys_pressed['w']:
            dy -= 2
        if keys_pressed['s']:
            dy += 2
        if keys_pressed['a']:
            dx -= 2
        if keys_pressed['d']:
            dx += 2
        
        if dx != 0 or dy != 0:
            collision_x1, collision_y1, collision_x2, collision_y2 = map_canvas.bbox('character')
            collision_x1 += dx
            collision_x2 += dx
            collision_y1 += dy
            collision_y2 += dy
            list_of_overlaps_tags = check_for_overlaps(collision_x1, collision_y1, collision_x2, collision_y2)
           
        
            if can_move(list_of_overlaps_tags) == True:
                map_canvas.move(character, dx, dy)
            # if 'wall' in list_of_overlasps_tags:
            #     print('найдено пересечание')
            # if 'enemy' in list_of_overlasps_tags:
            #     print('найдено пересечание')
    
        # Повторяем каждые 16 мс (~60 кадров в секунду)
    main_window.after(16, character_movement)



def make_choice():
    if battle_canvas.coords(cursor)[1] == 234.5:
        print('block')
    if battle_canvas.coords(cursor)[1] == 204.5:
        print('attack')

def update_hp_bars():
    battle_canvas.scale('pc_bar', 0, 0, player_battle_hp_x_din, 1)
    battle_canvas.scale('enemy_bar', 0, 0, enemy_battle_hp_x_din, 1)
    print(player_battle_hp_x_din, enemy_battle_hp_x_din)
    main_window.after(90, update_hp_bars)

def cursor_movement():
    rate_of_update = 6
    if game_states['battle'] == True:
        dx = 0
        dy = 0
        if keys_pressed['w'] and battle_canvas.coords(cursor)[1] > 205:
            dy -= 30
        if keys_pressed['s'] and battle_canvas.coords(cursor)[1] < 234:
            dy += 30
        #print(battle_canvas.coords(cursor))
        battle_canvas.move(cursor, dx, dy)
    main_window.after(16*rate_of_update, cursor_movement)

def press_enter():
    if game_states['battle'] == True:
        if keys_pressed['Return'] == True:
            #print('enter is pressed')
            make_choice()
    main_window.after(16, press_enter)

character_movement()
key_for_map_state()
cursor_movement()
press_enter()
update_hp_bars()

# Привязываем обработчики событий
main_window.bind("<KeyPress>", key_pressed)
main_window.bind("<KeyRelease>", key_released)


main_window.mainloop()