from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to our page")
window.geometry('2500x1500')
window.configure(background = "gray")
ttk.Button(window, text = "Hai,I m Navin").grid()
ttk.Button(window, text = "Welcome").grid()
window.mainloop()