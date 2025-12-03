import tkinter
from game_window import main_window

def change_to_battle():
    main_window.map_frame.pack_forget()
    main_window.battle_frame.pack()

def change_to_map():
    main_window.battle_frame_frame.pack_forget()
    main_window.map_frame_frame.pack()