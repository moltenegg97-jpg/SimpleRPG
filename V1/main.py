import tkinter
from game_window import main_window
import map
import keys
import game_state_control #сейчас для теста/ или нет
import battle 

def refresh_map():
    map.move_pc()
    main_window.main_window.after(16, refresh_map)

def main():
    map.draw_map()
    map.draw_characters()
    refresh_map()
    battle.draw_icons()
    battle.draw_hp_bars()

    
    
    main_window.main_window.bind("<KeyPress>", keys.key_pressed)
    main_window.main_window.bind("<KeyRelease>", keys.key_released)
    
    main_window.map_frame.pack() #сейчас для теста
    game_state_control.change_to_battle() #сейчас для теста

    main_window.main_window.mainloop()

if __name__ == '__main__':
    main()