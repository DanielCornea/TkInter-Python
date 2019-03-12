from tkinter import *

class App: 
    def __init__(self, master): 
        # the main frame 
        frame = Frame(master)
        frame.pack()
        

        # labeled frame
        group = LabelFrame(frame, text = "Group", padx = 5, pady = 5, bd = 5, fg = "green")
        group.pack(padx = 10, pady = 10)

        w = Entry(group)
        w.pack 
       

        # left = Label(m, text = "right pane")
        # m.add(left)

        # right = Label(m, text = "right pane")
        # m.add(right)

        print("added panes")

        self.button = Button(
            group, text = "QUIT", fg = "red", command = frame.quit
        )
        self.button.pack(side = LEFT)

        self.hi_there = Button(
            group, text = "HELLO", command = self.say_hi
        )
        self.hi_there.pack(side = LEFT)

        print("butons added")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
# root.destroy()