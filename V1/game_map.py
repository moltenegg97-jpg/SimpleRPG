import tkinter
from game_window import main_window 
import keys 
from game_state_control import game_state
import game_objects
import battle
from battle_system import battle_system
import effects

#import game_window импортировать для теста из модуля

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

def draw_map():
    for i in range(len(map_matrix)):
        for j in range(len(map_matrix[i])):
            if map_matrix[i][j] == 1:
                color = 'blue'
                layer = 'wall'
            if map_matrix[i][j] == 0:
                color = 'green'
                layer = 'background'
            main_window.map_canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill=color, outline="black", tags=layer)

def spawn_enemy_by_sprite(sprite, type:str, obj_id:str):
    obj_name = game_objects.spawn_enemy(type, obj_id)
    game_objects.enemy_dict[sprite] = obj_name
    return obj_name

def draw_items():
    game_objects.potion1.spawn(50, 30)
    game_objects.potion2.spawn(50, 50)
    game_objects.sword.spawn(25, 40)

def draw_characters():
    playerY = 30
    playerX = 30
    character = main_window.map_canvas.create_oval(playerY, playerX, playerY+8, playerX+8, fill = 'yellow', outline='black', tags='character')

    goblin_sprite1 = main_window.map_canvas.create_oval(40, 100, 48, 108, fill='red', outline='black', tags='enemy')
    spawn_enemy_by_sprite(goblin_sprite1, 'Goblin', '1')
    goblin_sprite2 = main_window.map_canvas.create_oval(70, 80, 78, 88, fill='red', outline='black', tags='enemy')
    spawn_enemy_by_sprite(goblin_sprite2, 'Goblin', '2')

    
def get_list_of_overlaps(dx, dy)->dict:
    list_of_overlaps = {}
    collision_x1, collision_y1, collision_x2, collision_y2 = main_window.map_canvas.bbox('character') #bbbox -> tuple
    collision_x1 += dx
    collision_x2 += dx
    collision_y1 += dy
    collision_y2 += dy
    overlaps_id: tuple = (main_window.map_canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2))

    for i in overlaps_id:       
        if len(main_window.map_canvas.gettags(i))> 0:
            if main_window.map_canvas.gettags(i)[0] in list_of_overlaps:        
                list_of_overlaps[main_window.map_canvas.gettags(i)[0]].append(i)
            else:
                list_of_overlaps[main_window.map_canvas.gettags(i)[0]] = [i]
    return list_of_overlaps

def delete_object(obj_id):
    del game_objects.enemy_dict[obj_id] #удаляет из словаря объектов
    main_window.map_canvas.delete(obj_id) #удаляет с карты

def delete_item(obj_id):
    #del game_objects.item_dict[obj_id]
    main_window.map_canvas.delete(obj_id)

def start_battle(obj_id):
    game_state.change_to_battle(obj_id)
    battle.draw_hp_bars()
    #main_window.main_window.after(300, battle_system.active_battle)
    battle_system.active_battle()

def can_move(dx, dy)->bool:
    list_of_overlaps = get_list_of_overlaps(dx, dy)
    if 'wall' in list_of_overlaps:
        return False
    if 'item' in list_of_overlaps:
        #print(list_of_overlaps['item'][0])
        #print(game_objects.item_dict)
        #print(game_objects.item_dict[list_of_overlaps['item'][0]])
        game_objects.item_dict[list_of_overlaps['item'][0]].pick_up()
        delete_item(list_of_overlaps['item'][0])        
    if 'enemy' in list_of_overlaps:
        start_battle(game_objects.enemy_dict[list_of_overlaps['enemy'][0]]) #задел на переход в бой
        delete_object(list_of_overlaps['enemy'][0])
    return True


def move_pc():
    dx, dy = 0, 0
    x, y = main_window.map_canvas.coords('character')[0], main_window.map_canvas.coords('character')[1]
    if keys.list_of_keys['w']:
        dy -= 2
    if keys.list_of_keys['s']:
        dy += 2
    if keys.list_of_keys['a']:
        dx -= 2
    if keys.list_of_keys['d']:
        dx += 2

    if keys.list_of_keys['u']:
        print(game_objects.enemy_dict)
    if keys.key_tapped['i']:
        game_state.change_to_inventory()
    keys.reset_input_flags()
    
        

    if (dx != 0 or dy != 0) and can_move(dx, dy):
        effects.make_sparks(x, y, -dx, -dy, 1)
        main_window.map_canvas.move('character', dx, dy)

if __name__ == '__main__':
    
    #game_window.main_window.map_frame.pack() #импортировать game_window для теста из модуля
    draw_map()
    draw_characters()
    #game_window.main_window.main_window.mainloop() #импортировать game_window для теста из модуля