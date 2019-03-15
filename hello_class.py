from tkinter import *

class App: 
    def __init__(self, master): 
        # the main frame 
        frame = Frame(master)
        frame.pack(fill = BOTH)

        first_row = Label(frame, text="Red", bg="red", fg="white")
        first_row.pack(fill=BOTH)
  
        second_row = Label(frame, text="Green", bg="green", fg="black")
        second_row.pack(fill=BOTH)
  
        third_row = Label(frame, text="Blue", bg="blue", fg="white")
        third_row.pack(fill=BOTH)

        fourth_row = Label(frame, text="Yellow", bg="yellow", fg="white")
        fourth_row.pack(fill=BOTH)

        fifth_row = Label(frame, text="Yellow", bg="yellow", fg="white")
        fifth_row.pack(fill = BOTH)


        button_0 = Button(fifth_row, text = "0")
        button_0.pack(side = LEFT)

        button_equals = Button(fifth_row, text = "=")
        button_equals.pack(side = LEFT)

        button_1 = Button(fourth_row, text = "1")
        button_1.pack( side = LEFT)

        button_2 = Button(fourth_row, text = "2")
        button_2.pack(side = LEFT)

        button_3 = Button(fourth_row, text = "3")
        button_3.pack(side = LEFT)

        button_4 = Button(third_row, text = "4")
        button_4.pack(side = LEFT)

        button_5 = Button(third_row, text = "5")
        button_5.pack(side = LEFT)

        button_6 = Button(third_row, text = "6")
        button_6.pack(side = LEFT)

        button_7 = Button(second_row, text = "7")
        button_7.pack(side = LEFT)

        button_8 = Button(second_row, text = "8")
        button_8.pack(side = LEFT)

        button_9 = Button(second_row, text = "9")
        button_9.pack(side = LEFT)

        
















        # panned window 
        # m = PanedWindow(orient = VERTICAL)
        # m.pack(fill = BOTH, expand = 5)











        # first_pane = Label(m, bg = "green")
        # first_pane.pack()
        
            
        # first_pane = Label(m, text = "first_pane", bg = "green")
        # m.add(first_pane)

        
        # second_pane = Label(m, text = "second_pane")
        # m.add(second_pane)
    

        # third_pane = Label(m, text = "third_pane")
        # m.add(third_pane)

        # fourth_pane = Label(m, text = "fourth_pane")
        # m.add(fourth_pane)

        # fifth_pane = Label(m, text = "fifth_pane", bg = "green")
        # m.add(fifth_pane)



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