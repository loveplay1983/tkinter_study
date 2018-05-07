from tkinter import *

master = Tk()
# w = Scale(master, from_=0, to=100)
w = Scale(master, from_=0, to=100, orient=HORIZONTAL, width=20, label='test', length=600)
w.pack()

mainloop()