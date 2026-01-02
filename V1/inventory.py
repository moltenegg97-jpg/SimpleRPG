import keys
from game_state_control import game_state
import tkinter
from game_window import main_window
import game_objects
layout = [[1, 1],
          [1, 1],
          [1, 1],
          [],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

tile_size = 30

def draw_inventory():
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == 1:
                main_window.inventory_canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill="grey", outline="black", tags='inv_bg')
            if layout[i][j] == 0:
                main_window.inventory_canvas.create_rectangle(j*tile_size, i*tile_size, j*tile_size+tile_size, i*tile_size+tile_size, fill="grey", outline="black", tags='inv_bg')



class Cursor():
    def __init__(self):
        self.cursor_pos_x = 0
        self.cursor_pos_y = 0
        cursor_x = 95
        cursor_y = 205
        self.cursor_jp_x = tile_size
        self.cursor_jp_y = tile_size
        cursor_diam = 5
        self.cursor = main_window.inventory_canvas.create_rectangle(0*tile_size, 0*tile_size, 0*tile_size+tile_size, 0*tile_size+tile_size, outline='red', tags='cursor')
        self.choice_callback = None

    def set_choice_callback(self, callback):
        self.choice_callback = callback

    def move_cursor(self):
        dx, dy = 0, 0
        if keys.key_tapped['w']: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_y -= 1
            dy -= self.cursor_jp_y
            keys.reset_input_flags()
        if keys.key_tapped['s']: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_y += 1
            dy += self.cursor_jp_y
            keys.reset_input_flags()
        if keys.key_tapped['a']: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_x -= 1
            dx -= self.cursor_jp_x
            keys.reset_input_flags()
        if keys.key_tapped['d']: #ограничения по передвижению курсора, можно улучшить позже
            self.cursor_pos_x +=1
            dx += self.cursor_jp_x
            keys.reset_input_flags()

        main_window.inventory_canvas.move(self.cursor, dx, dy)

    def use_item(self) -> bool: #if true - turn ended
        if keys.key_tapped['Return']:
            print('key is pressed') #для теста, удалить позже
            print(self.cursor_pos_x, self.cursor_pos_y)
            obj_id = layout[self.cursor_pos_y][self.cursor_pos_x]
            print(obj_id)
            if self.cursor_pos_y < 3:
                if obj_id in game_objects.item_dict:
                    print(game_objects.item_dict[obj_id])
                    game_objects.item_dict[obj_id].de_equip()
                    keys.reset_input_flags()
                    if game_state.previous_state == 'battle':
                        if self.choice_callback:
                            self.choice_callback('inventory')
                        game_state.back_from_inventory()
                    return

            if obj_id in game_objects.item_dict:
                print(game_objects.item_dict[obj_id])
                game_objects.item_dict[obj_id].use()
                if game_objects.item_dict[obj_id].consumable:
                    del game_objects.item_dict[obj_id]
                if game_state.previous_state == 'battle':
                    if self.choice_callback:
                        self.choice_callback('inventory')
                    game_state.back_from_inventory()
            else:
                print('cell is empty')
            keys.reset_input_flags()
            
        



def exit_inventory():
    if keys.key_tapped['i']:
        game_state.back_from_inventory()
        keys.reset_input_flags()

inv_cursor = Cursor()