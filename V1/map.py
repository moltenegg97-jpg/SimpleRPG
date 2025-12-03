import tkinter
from game_window import main_window 
from keys import list_of_keys
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

    

if __name__ == '__main__':
    
    game_window.main_window.map_frame.pack() #импортировать game_window для теста из модуля
    draw_map()
    draw_characters()
    game_window.main_window.main_window.mainloop() #импортировать game_window для теста из модуля