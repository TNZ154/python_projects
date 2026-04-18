from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Virus Alert", "Your computer is infected with a virus. Please click OK to remove it.")
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)
root.mainloop()