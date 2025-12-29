import tkinter

class MainWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.map_frame = tkinter.Frame(self.main_window)
        self.battle_frame = tkinter.Frame(self.main_window)
        self.map_canvas = tkinter.Canvas(self.map_frame)
        self.battle_canvas = tkinter.Canvas(self.battle_frame)
        self.battle_log = tkinter.Text(self.battle_frame, height=5, takefocus=0, state=tkinter.DISABLED)
        #self.map_frame.pack() #only for test
        self.map_canvas.pack()
        self.battle_canvas.pack()
        self.battle_log.pack()
    
    def add_battle_log(self, message):
        self.battle_log.configure(state=tkinter.NORMAL)
        self.battle_log.insert('end', f'{message}\n')
        self.battle_log.see('end')
        self.battle_log.configure(state=tkinter.DISABLED)


main_window = MainWindow()

if __name__ == '__main__':
    main_window.main_window.mainloop()