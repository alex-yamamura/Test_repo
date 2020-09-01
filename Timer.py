from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import time


def timer():
    pass


def add_timer():
    pass


root = ThemedTk(theme='breeze')
root.title('Pyrna')
root.geometry('600x400+500+200')
root.resizable(0, 0)

button_start = ttk.Button(root, text='Старт', command=timer)
button_start.place(relx=0.75, rely=0.1)

button_add = ttk.Button(root, text='Добавить таймер')
button_add.place(relx=0.75, rely=0.2)

CurrentTime = time.monotonic()

label = ttk.Label(root, text=CurrentTime, font='Arial 30 bold')
label.place(relx=0.1, rely=0.1)

root.mainloop()
