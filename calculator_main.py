from tkinter import * 
#root window
root  = Tk()
root.minsize(500, 450) # seeting the minimum size

# setting the calculator screen as a string variable
calc_text = StringVar()
# emptying the string variable 
calc_text.set("")

#####################################################
#                                                   #
#            Back-end functions                     #
#                                                   #
#####################################################

# as a rule, the bellow functions take the text on the
# calc screen and append the respective number/operation

# second row 
def button_slash() :
        calc_text.set(calc_text.get() + "/")

# clearing the screen
def button_clear() :
        calc_text.set("")

# third row 
def button_seven() :
        calc_text.set(calc_text.get() + "7")

def button_eight() :
        calc_text.set(calc_text.get() + "8")

def button_nine() :
        calc_text.set(calc_text.get() + "9")

def button_multi() :
        calc_text.set(calc_text.get() + "*")

# fourth row
def button_four() :
        calc_text.set(calc_text.get() + "4")

def button_five() :
        calc_text.set(calc_text.get() + "5")

def button_six() :
        calc_text.set(calc_text.get() + "6")

# fifth row 
def button_minus() :
        calc_text.set(calc_text.get() + "-")
def button_one() :
        calc_text.set(calc_text.get() + "1")

def button_two() :
        calc_text.set(calc_text.get() + "2")

def button_three() :
        calc_text.set(calc_text.get() + "3")

# sixth row
def button_plus() :
        calc_text.set(calc_text.get() + "+")

def button_zero() :
        calc_text.set(calc_text.get() + "0")

def button_dot() :
        calc_text.set(calc_text.get() + ".")

# the longest function the "=", it evaluates the expresion 
def button_equals() : 
        # try catch block in case user messes up 
        try : 
                # taking the expression from the screen 
                expr = calc_text.get()

                # these variables are used for negative numbers
                minus = 1.0
                minus2 = 1.0
                
                # here we remove the first minus in the expression
                # and assign the -1 to the minus variable 
                if (expr[0] == "-") :
                        minus = -1.0
                        expr = expr[1:]
                # in case of an expression such as 2--2 we transform the "--" in "+" 
                if (expr.find("--") > -1) :
                        expr = expr.replace("--", "+")
                
                # in case the second number is a minus we assign -1 to the minus 2 
                # and remove the "-"
                if (expr.find("*-") > -1) :
                        expr = expr.replace("-", "")
                        minus2 = -1.0
                
                # same as above only with the "/" operator
                if (expr.find("/-") > -1) :
                        expr = expr.replace("-", "")
                        minus2 = -1.0
              
                # the addition operation 
                # as you can see if the first number gets multiplied by minus
                # in case the initial number is negative minus is -1 
                # otherwise the minus is 1 
                if (expr[expr.find("+")] == "+") :
                        result = expr.split("+")
                        calc_text.set(float(result[0])*minus + float(result[1]))
                        return

                # division operation 
                # notice the placement of the minus and minus2 variables 
                if (expr[expr.find("/")] == "/") :
                        result = expr.split("/")
                        calc_text.set(round(float(result[0])*minus / float(result[1])*minus2, 2))
                        return
                        
                # substraction operation 
                if (expr[expr.find("-")] == "-") :
                        result = expr.split("-")
                        calc_text.set(float(result[0])*minus - float(result[1]))
                        return
             
                # multiplication                 
                if (expr[expr.find("*")] == "*") :
                        result = expr.split("*")
                        calc_text.set(float(result[0])*minus * float(result[1])*minus2)
                        return
       
                # because at the end of each if there is a return
                # in case none of the above cases apply it raises an error
                raise("it reached the end something not cool")
        
        except : 
                calc_text.set("operation not possible")
        

#####################################################
#                                                   #
#            Front-end functions                    #
#                                                   #
#####################################################

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