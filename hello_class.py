from tkinter import *

class App: 
    def __init__(self, master): 
        # the main frame 
        frame = Frame(master)
        frame.pack(padx=2, pady=2)

        # panned window 
        m = PanedWindow(orient = VERTICAL)
        m.pack(fill = BOTH, expand = 5)

        # first_pane = Label(m, bg = "green")
        # first_pane.pack()
        
            
        first_pane = Label(m, text = "first_pane", bg = "green")
        m.add(first_pane)

        
        second_pane = Label(m)
        m.add(second_pane)
    

        third_pane = Label(m, text = "third_pane")
        third_pane.pack()

        fourth_pane = Label(m, text = "fourth_pane")
        fourth_pane.pack()

        fifth_pane = Label(m, text = "fifth_pane")
        fifth_pane.pack()



    #     left = Label(m, text = "right pane")
    #     m.add(left)

    #     right = Label(m, text = "right pane")
    #     m.add(right)

    #     print("added panes")

    #     self.button = Button(
    #         left, text = "QUIT", fg = "red", command = frame.quit
    #     )
    #     self.button.pack(side = LEFT)

    #     self.hi_there = Button(
    #         right, text = "HELLO", command = self.say_hi
    #     )
    #     self.hi_there.pack()

    #     print("butons added")

    # def say_hi(self):
    #     print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
# root.destroy()