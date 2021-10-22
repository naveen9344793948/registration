from tkinter import *
from tkinter import ttk
window = Tk()
window.title("welcome to Registeration Form")
window.geometry('450x300')
window.configure(background = "black")
a = Label(window , text = "first Name ").grid(row = 0,column = 0)
b = Label(window , text = "last Name").grid(row = 1 ,column = 0)
c = Label(window , text = "E-mail Id").grid(row = 2 ,column = 0)
d = Label(window , text = "password").grid(row = 3 ,column = 0)
e = Label(window , text = "Address").grid(row = 4 ,column = 0)
f = Label(window , text ="contact no").grid(row =5 ,column =0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
f1 = Entry(window).grid(row = 5,column = 1)
def clicked():
    res ="Welcome to" + txt.get()
    lbl.configure(text= res)
btn = ttk . Button(window ,text="submit").grid(row=6,column=0)
window.mainloop()


















