import tkinter


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

for i in range(len(map_matrix)):
    for j in range(len(map_matrix[i])):
        if map_matrix[i][j] == 1:
            color = 'blue'
            layer = 'wall'
        if map_matrix[i][j] == 0:
            color = 'green'
            layer = 'background'
        map_canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill=color, outline="black", tags=layer)

playerY = 30
playerX = 30
character = map_canvas.create_oval(playerY, playerX, playerY+8, playerX+8, fill = 'yellow', outline='black', tags='character')

goblin1 = map_canvas.create_oval(40, 100, 48, 108, fill='red', outline='black', tags='enemy')
goblin2 = map_canvas.create_oval(70, 80, 78, 88, fill='red', outline='black', tags='enemy')

battle_canvas.create_rectangle(50, 50, 60, 60, fill = 'yellow', outline='black')
battle_canvas.create_rectangle(90, 50, 100, 60, fill = 'red', outline='black')

keys_pressed = {
    'w': False,
    'a': False, 
    's': False,
    'd': False,
    'u': False,
    'i': False
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
            map_canvas.delete(list_of_overlaps['enemy'][0])
            # map_canvas.delete('enemy')
            return False
    return True

def to_battle_state():
    if keys_pressed['u']:
        map_canvas.pack_forget()
        battle_canvas.pack()
        game_states['map'] = False
        game_states['battle'] = True
    main_window.after(16, to_battle_state)

def to_map_state():
    if keys_pressed['i']:
        battle_canvas.pack_forget()
        map_canvas.pack()
        game_states['battle'] = False
        game_states['map'] = True
    main_window.after(16, to_map_state)


# Функция, которая периодически проверяет состояние клавиш и двигает персонажа
def character_movment():
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
            overlaps_id = (map_canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2))
            list_of_overlasps_tags = {}
            print(overlaps_id)
        
            for i in overlaps_id:
            
                #list_of_overlasps_tags.append(map_canvas.gettags(i)[0])
                if map_canvas.gettags(i)[0] in list_of_overlasps_tags:
                    print('такой тег был')
                    print(list_of_overlasps_tags[map_canvas.gettags(i)[0]])
                    list_of_overlasps_tags[map_canvas.gettags(i)[0]].append(i)
                else:
                    list_of_overlasps_tags[map_canvas.gettags(i)[0]] = [i]
        
            #print(collision_x1, collision_y1, collision_x2, collision_y2)
            print(map_canvas.bbox(character))
            print(list_of_overlasps_tags)
        
            if can_move(list_of_overlasps_tags) == True:
                map_canvas.move(character, dx, dy)
            # if 'wall' in list_of_overlasps_tags:
            #     print('найдено пересечание')
            # if 'enemy' in list_of_overlasps_tags:
            #     print('найдено пересечание')
    
        # Повторяем каждые 16 мс (~60 кадров в секунду)
        main_window.after(16, character_movment)
character_movment()
to_battle_state()
to_map_state()
# Привязываем обработчики событий
main_window.bind("<KeyPress>", key_pressed)
main_window.bind("<KeyRelease>", key_released)

# print(map_canvas.bbox('character'))
# x1, y1, x2, y2 = map_canvas.bbox('character')
# print(map_canvas.find_overlapping(x1, y1, x2, y2))
# list_of_overlaps = list(map_canvas.find_overlapping(x1, y1, x2, y2))

# for i in range(len(list_of_overlaps)):
#     print(map_canvas.gettags(list_of_overlaps[i]))

main_window.mainloop()