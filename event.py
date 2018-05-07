"""
what to do ??
1. click event
2. status event
3. window event (open, quit, or handler )
-----------------------------------------------------------
how to accomplish ??
1. command (callbacks)
2. bind
3. protocol
------------------------------------------------------------
"""

from tkinter import *

# from tkinter import
root = Tk()

# command event
if False:
    def btn1_click():
        print('btn1 has clicked')


    btn1 = Button(root, text='hi', command=btn1_click)
    btn1.pack()
    root.mainloop()

# bind event
if False:
    def callback(event):
        frame.focus_set()
        print('Coordinate at: ', event.x, event.y)


    def key(event):
        print('You pressed: ', str(event.char))


    frame = Frame(root, bg='purple', width=400, height=500)
    frame.bind('<Key>', key)
    frame.bind('<Button-1>', callback)
    frame.pack()

    root.mainloop()

# protocol event
if True:
    from tkinter import messagebox
    """
    The Toplevel widget work pretty much like Frame, but it is displayed in a 
    separate, top-level window. Such windows usually have title bars, borders, 
    and other “window decorations”.
    """
    top = Toplevel(bg='yellow', width=500, height=300)
    top.protocol('WM_DELETE_WINDOW', top.destroy)

    def callback():
        if messagebox.askokcancel('Quit', 'Do you want to quit???'):
            root.destroy()

    root.protocol('WM_DELETE_WINDOW', callback)
    root.mainloop()
