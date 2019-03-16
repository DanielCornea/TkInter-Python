import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
#root window
root  = tk.Tk()

# The label is instantiated root is the parent 
# # label is used to display text and bitmap image
# my_label  = tk.Label(root, text = "Hello World!!!", fg="green")
# my_label.pack()

name = tk.StringVar()

def get_text():
    print(name_entered.get())
    mBox.Message(name_entered.get())



name_entered = tk.Entry(root, width = 40, textvariable = name)
name_entered.pack()

button1 = tk.Button(
            root, text = "print text", command = get_text
        )

        
button1.pack()
root.mainloop()

