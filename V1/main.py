import tkinter
from game_window import main_window
import game_map
import keys
from game_state_control import game_state #сейчас для теста/ или нет
import battle 
from battle_system import battle_system
import inventory


refresh_rate = 16


def refresh_map():
    if game_state.state['map']:
        game_map.move_pc()
    main_window.main_window.after(refresh_rate, refresh_map)

def refresh_battle():
    if game_state.state['battle']:
        battle.battle_action()
        #if battle_system.isPlayerturn:
        #    battle.cursor.move_cursor()
        #    battle.cursor.pick_battle_option()
        battle.exit_battle()
    main_window.main_window.after(refresh_rate, refresh_battle) #временно для теста

def refresh_inventory():
    if game_state.state['inventory']:
        main_window.inventory_canvas.tag_raise('cursor', 'inv_bg')
        inventory.exit_inventory()
        inventory.inv_cursor.move_cursor()
        inventory.inv_cursor.use_item()
    main_window.main_window.after(refresh_rate, refresh_inventory)

def print_states():
    if keys.key_tapped['y']:
        print(game_state.state)
        keys.reset_input_flags()
    main_window.main_window.after(refresh_rate, print_states)

def main():
    game_map.draw_map()
    game_map.draw_characters()
    game_map.draw_items()
    refresh_map()
    battle.draw_icons()
    battle.draw_battle_options()
    inventory.draw_inventory()
    print_states()
    
    refresh_battle() #временно для теста
    refresh_inventory()
    
    main_window.main_window.bind("<KeyPress>", keys.key_pressed)
    main_window.main_window.bind("<KeyRelease>", keys.key_released)
    
    game_state.change_to_map() #сейчас для теста
    #game_state.change_to_battle() #сейчас для теста

    main_window.main_window.mainloop()

if __name__ == '__main__':
    main()

