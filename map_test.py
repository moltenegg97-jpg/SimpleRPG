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
        if map_matrix[i][j] == 0:
            color = 'green'
        canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill=color, outline="black")



main_window.mainloop()