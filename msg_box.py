from tkinter import messagebox
from tkinter import *

root = Tk()
root.config(cursor='gumby')

def callback():
    if messagebox.askyesno('Title', 'Message Box'):
        print('Clicked yes')
    else:
        print('Clicked no')


button = Button(root, text='Btn1', command=callback)
button.config()
button.pack()
root.mainloop()
