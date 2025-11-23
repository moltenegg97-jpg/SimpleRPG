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
canvas = tkinter.Canvas(main_window)
canvas.pack()
# canvas.create_rectangle(50, 50, 70, 70, fill="blue", outline="black")
# canvas.create_rectangle(200, 200, 220, 220, fill="green", outline="black")

for i in range(len(map_matrix)):
    for j in range(len(map_matrix[i])):
        if map_matrix[i][j] == 1:
            color = 'blue'
            layer = 'wall'
        if map_matrix[i][j] == 0:
            color = 'green'
            layer = 'background'
        canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill=color, outline="black", tags=layer)

playerY = 30
playerX = 30
character = canvas.create_oval(playerY, playerX, playerY+8, playerX+8, fill = 'yellow', outline='black', tags='character')

keys_pressed = {
    'w': False,
    'a': False, 
    's': False,
    'd': False
}


def key_pressed(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True

def key_released(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False

# Функция, которая периодически проверяет состояние клавиш и двигает персонажа
def character_movment():
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
        collision_x1, collision_y1, collision_x2, collision_y2 = canvas.bbox('character')
        collision_x1 += dx
        collision_x2 += dx
        collision_y1 += dy
        collision_y2 += dy
        list_of_overlaps = list((canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2)))
        print(f'кортеж: {canvas.find_overlapping(collision_x1, collision_y1, collision_x2, collision_y2)}')
        list_of_overlasps_tags = []
        for i in range(len(list_of_overlaps)):
            list_of_overlasps_tags.append(canvas.gettags(list_of_overlaps[i]))
        print(collision_x1, collision_y1, collision_x2, collision_y2)
        print(canvas.bbox(character))
        print(list_of_overlasps_tags)
        if ('wall',) not in list_of_overlasps_tags:
            canvas.move(character, dx, dy)
        if ('wall',) in list_of_overlasps_tags:
            print('найдено пересечание')
    
    # Повторяем каждые 16 мс (~60 кадров в секунду)
    main_window.after(16, character_movment)
character_movment()
# Привязываем обработчики событий
main_window.bind("<KeyPress>", key_pressed)
main_window.bind("<KeyRelease>", key_released)

# print(canvas.bbox('character'))
# x1, y1, x2, y2 = canvas.bbox('character')
# print(canvas.find_overlapping(x1, y1, x2, y2))
# list_of_overlaps = list(canvas.find_overlapping(x1, y1, x2, y2))

# for i in range(len(list_of_overlaps)):
#     print(canvas.gettags(list_of_overlaps[i]))

main_window.mainloop()