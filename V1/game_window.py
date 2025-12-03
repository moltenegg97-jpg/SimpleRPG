import tkinter

class MainWindow:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.map_frame = tkinter.Frame(self.main_window)
        self.battle_frame = tkinter.Frame(self.main_window)
        self.map_canvas = tkinter.Canvas(self.map_frame)
        self.battle_canvas = tkinter.Canvas(self.battle_frame)
        #self.map_frame.pack() #only for test
        self.map_canvas.pack()
        self.battle_canvas.pack()

main_window = MainWindow()

if __name__ == '__main__':
    main_window.main_window.mainloop()