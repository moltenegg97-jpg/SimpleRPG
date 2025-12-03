import tkinter
from game_window import main_window
import map
import keys
from game_state_control import game_state #сейчас для теста/ или нет
import battle 

def refresh_map():
    if game_state.state['map']:
        map.move_pc()
    main_window.main_window.after(16, refresh_map)

def refresh_battle():
    if game_state.state['battle']:
        battle.battle_action()
        battle.exit_battle()
    main_window.main_window.after(16*8, refresh_battle) #временно для теста

def main():
    map.draw_map()
    map.draw_characters()
    refresh_map()
    battle.draw_icons()
    battle.draw_hp_bars()
    refresh_battle() #временно для теста
    
    
    main_window.main_window.bind("<KeyPress>", keys.key_pressed)
    main_window.main_window.bind("<KeyRelease>", keys.key_released)
    
    game_state.change_to_map() #сейчас для теста
    #game_state.change_to_battle() #сейчас для теста

    main_window.main_window.mainloop()

if __name__ == '__main__':
    main()