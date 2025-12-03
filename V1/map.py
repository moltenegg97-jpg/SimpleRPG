import tkinter
from game_window import main_window 
from keys import list_of_keys
from game_state_control import game_state
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

def draw_characters():
    playerY = 30
    playerX = 30
    character = main_window.map_canvas.create_oval(playerY, playerX, playerY+8, playerX+8, fill = 'yellow', outline='black', tags='character')

    goblin1 = main_window.map_canvas.create_oval(40, 100, 48, 108, fill='red', outline='black', tags='enemy')
    goblin2 = main_window.map_canvas.create_oval(70, 80, 78, 88, fill='red', outline='black', tags='enemy')

    
def get_list_of_overlaps(dx, dy)->dict:
    list_of_overlaps = {}
    collision_x1, collision_y1, collision_x2, collision_y2 = main_window.map_canvas.bbox('character') #bbbox -> tuple
    collision_x1 += dx
    collision_x2 += dx
    collision_y1 += dy
    collision_y2 += dy
    overlaps_id: tuple = (main_window.map_canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2))

    for i in overlaps_id:            
        #list_of_overlasps_tags.append(map_canvas.gettags(i)[0])
        if main_window.map_canvas.gettags(i)[0] in list_of_overlaps:        
            list_of_overlaps[main_window.map_canvas.gettags(i)[0]].append(i)
        else:
            list_of_overlaps[main_window.map_canvas.gettags(i)[0]] = [i]
    return list_of_overlaps

def can_move(dx, dy)->bool:
    if 'wall' in get_list_of_overlaps(dx, dy):
        return False
    if 'enemy' in get_list_of_overlaps(dx, dy):
        game_state.change_to_battle() #задел на переход в бой
    return True


def move_pc():
    dx, dy = 0, 0
    
    if list_of_keys['w']:
        dy -= 2
    if list_of_keys['s']:
        dy += 2
    if list_of_keys['a']:
        dx -= 2
    if list_of_keys['d']:
        dx += 2

    if (dx != 0 or dy != 0) and can_move(dx, dy):
        main_window.map_canvas.move('character', dx, dy)

if __name__ == '__main__':
    
    #game_window.main_window.map_frame.pack() #импортировать game_window для теста из модуля
    draw_map()
    draw_characters()
    #game_window.main_window.main_window.mainloop() #импортировать game_window для теста из модуля