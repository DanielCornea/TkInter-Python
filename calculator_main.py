from tkinter import * 
#root window
root  = Tk()
root.minsize(500, 450) # seeting the minimum size



calc_text = StringVar()
calc_text.set("")

def button_slash() :
        calc_text.set(calc_text.get() + "/")

def button_clear() :
        calc_text.set("")


def button_seven() :
        calc_text.set(calc_text.get() + "7")

def button_eight() :
        calc_text.set(calc_text.get() + "8")

def button_nine() :
        calc_text.set(calc_text.get() + "9")

def button_multi() :
        calc_text.set(calc_text.get() + "*")

def button_four() :
        calc_text.set(calc_text.get() + "4")

def button_five() :
        calc_text.set(calc_text.get() + "5")

def button_six() :
        calc_text.set(calc_text.get() + "6")

def button_minus() :
        calc_text.set(calc_text.get() + "-")


def button_one() :
        calc_text.set(calc_text.get() + "1")

def button_two() :
        calc_text.set(calc_text.get() + "2")

def button_three() :
        calc_text.set(calc_text.get() + "3")

def button_plus() :
        calc_text.set(calc_text.get() + "+")


def button_zero() :
        calc_text.set(calc_text.get() + "0")

def button_dot() :
        calc_text.set(calc_text.get() + ".")

def button_equals() : 
        try : 
                expr = calc_text.get()
                minus = 1.0
                minus2 = 1.0
                if (expr.find("--") > -1) :
                        expr = expr.replace("--", "+")
                
                if (expr.find("*-") > -1) :
                        expr = expr.replace("-", "")
                        minus2 = -1
                if (expr.find("/-") > -1) :
                        expr = expr.replace("-", "")
                        minus2 = -1.0

                if (expr[0] == "-") :
                        minus = -1.0
                        expr = expr[1:]
                              
                if (expr[expr.find("+")] == "+") :
                        print("here")
                        result = expr.split("+")
                        calc_text.set(float(result[0])*minus + float(result[1]))
                        return

                if (expr[expr.find("/")] == "/") :
                        result = expr.split("/")
                        calc_text.set(float(result[0])*minus / float(result[1])*minus2)
                        
                if (expr[expr.find("-")] == "-") :
                        result = expr.split("-")
                        calc_text.set(float(result[0])*minus - float(result[1]))
                        return
                
                if (expr[expr.find("*")] == "*") :
                        result = expr.split("*")
                        calc_text.set(float(result[0])*minus * float(result[1])*minus2)
                        return
        
        except : 
                calc_text.set("operation not possible")

                
                
         




# setting equal weights for columns and rows
for row_index in range(6):
    Grid.rowconfigure(root, row_index, weight=1)
    for col_index in range(4):
        Grid.columnconfigure(root, col_index, weight=1)


# first row 
calc_screen = Label(root, textvariable = calc_text).grid(row = 0, columnspan = 4, sticky=N+S+E+W)

# second row
button_clear = Button(root, text = "C", command = button_clear).grid(row = 1, columnspan = 3, sticky=N+S+E+W)
button_slash = Button(root, text = "/", command = button_slash).grid(row = 1, column = 3, sticky=N+S+E+W)

# third row 
button_seven = Button(root, text = "7", command = button_seven).grid(row = 2, column = 0, sticky=N+S+E+W)
button_eight = Button(root, text = "8", command = button_eight).grid(row = 2, column = 1, sticky=N+S+E+W)
button_nine = Button(root, text = "9", command = button_nine).grid(row = 2, column = 2, sticky=N+S+E+W)
button_multi = Button(root, text = "*", command = button_multi).grid(row = 2, column = 3, sticky=N+S+E+W)

# fourth row 
button_four = Button(root, text = "4", command = button_four).grid(row = 3, column = 0, sticky=N+S+E+W)
button_five = Button(root, text = "5", command = button_five).grid(row = 3, column = 1, sticky=N+S+E+W)
button_six = Button(root, text = "6", command = button_six).grid(row = 3, column = 2, sticky=N+S+E+W)
button_minus = Button(root, text = "-", command = button_minus).grid(row = 3, column = 3, sticky=N+S+E+W)

# fifth row 
button_one = Button(root, text = "1", command = button_one).grid(row = 4, column = 0, sticky=N+S+E+W)
button_two = Button(root, text = "2", command = button_two).grid(row = 4, column = 1, sticky=N+S+E+W)
button_three = Button(root, text = "3", command = button_three).grid(row = 4, column = 2, sticky=N+S+E+W)
button_plus = Button(root, text = "+", command = button_plus).grid(row = 4, column = 3, sticky=N+S+E+W)

# six row 
button_zero = Button(root, text = "0", command = button_zero).grid(row = 5, column = 0, columnspan = 2, sticky=N+S+E+W)
button_dot = Button(root, text = ".", command = button_dot).grid(row = 5, column = 2, sticky=N+S+E+W)
button_equals = Button(root, text = "=", command = button_equals).grid(row = 5, column = 3, sticky=N+S+E+W)


root.mainloop()