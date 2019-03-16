from tkinter import * 
#root window
root  = Tk()
root.minsize(500, 450) # seeting the minimum size


# setting equal weights for columns and rows
for row_index in range(6):
    Grid.rowconfigure(root, row_index, weight=1)
    for col_index in range(4):
        Grid.columnconfigure(root, col_index, weight=1)

# first row 
calc_screen = Label(root, bg = "green").grid(row = 0, columnspan = 4, sticky=N+S+E+W)

# second row
button_clear = Button(root, text = "C").grid(row = 1, columnspan = 3, sticky=N+S+E+W)
button_slash = Button(root, text = "/").grid(row = 1, column = 3, sticky=N+S+E+W)

# third row 
button_seven = Button(root, text = "7").grid(row = 2, column = 0, sticky=N+S+E+W)
button_eight = Button(root, text = "8").grid(row = 2, column = 1, sticky=N+S+E+W)
button_nine = Button(root, text = "9").grid(row = 2, column = 2, sticky=N+S+E+W)
button_multi = Button(root, text = "*").grid(row = 2, column = 3, sticky=N+S+E+W)

# fourth row 
button_four = Button(root, text = "4").grid(row = 3, column = 0, sticky=N+S+E+W)
button_five = Button(root, text = "5").grid(row = 3, column = 1, sticky=N+S+E+W)
button_six = Button(root, text = "6").grid(row = 3, column = 2, sticky=N+S+E+W)
button_minus = Button(root, text = "-").grid(row = 3, column = 3, sticky=N+S+E+W)

# fifth row 
button_one = Button(root, text = "1").grid(row = 4, column = 0, sticky=N+S+E+W)
button_two = Button(root, text = "2").grid(row = 4, column = 1, sticky=N+S+E+W)
button_three = Button(root, text = "3").grid(row = 4, column = 2, sticky=N+S+E+W)
button_four = Button(root, text = "+").grid(row = 4, column = 3, sticky=N+S+E+W)

# six row 
button_zero = Button(root, text = "0").grid(row = 5, column = 0, columnspan = 2, sticky=N+S+E+W)
button_dot = Button(root, text = ".").grid(row = 5, column = 2, sticky=N+S+E+W)
button_equals = Button(root, text = "=").grid(row = 5, column = 3, sticky=N+S+E+W)


root.mainloop()