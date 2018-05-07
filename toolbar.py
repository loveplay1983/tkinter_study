from tkinter import *


root = Tk()


def callback():
    print('clicked tool bar button')


toolbar = Frame(root)
b = Button(toolbar, text='ne   w', width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

c = Button(toolbar, text='quit', width=6, command=callback)
c.pack(side=LEFT, padx=2, pady=2)

# toolbar.pack(side=TOP, fill=X)
toolbar.pack(side=TOP, fill=BOTH)

root.mainloop()

