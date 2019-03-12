from tkinter import *

class App: 
    def __init__(self, master): 
        # the main frame 
        frame = Frame(master)
        frame.pack()

        # panned window 
        m = PanedWindow(orient = HORIZONTAL)
        m.pack(fill = BOTH, expand = 1)

        left = Label(m, text = "right pane")
        m.add(left)

        right = Label(m, text = "right pane")
        m.add(right)

        print("added panes")

        self.button = Button(
            left, text = "QUIT", fg = "red", command = frame.quit
        )
        self.button.pack(side = LEFT)

        self.hi_there = Button(
            right, text = "HELLO", command = self.say_hi
        )
        self.hi_there.pack()

        print("butons added")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
# root.destroy()