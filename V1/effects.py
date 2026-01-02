import tkinter
import random
from game_window import main_window

def make_sparks(x, y, dx, dy, amount):
    oval_diam = 3
    delay = 60
    
    spark_sprite = main_window.map_canvas.create_oval(x, y, x+oval_diam, y+oval_diam, fill="#ad14d3", outline='black')
    
    if amount > 0:
        make_sparks(x, y, random.randint(-2, 2), random.randint(-2, 2), amount-1)
    
    def move_spark(remaining_steps):
        if remaining_steps > 0:
            # Передвигаем спрайт
            main_window.map_canvas.move(spark_sprite, dx, dy)
            # Планируем следующий шаг
            main_window.map_canvas.after(delay, lambda: move_spark(remaining_steps - 1))
        if remaining_steps == 0:
            main_window.map_canvas.delete(spark_sprite)

    main_window.map_canvas.after(delay, lambda: move_spark(4))
        