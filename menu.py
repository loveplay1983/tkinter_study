"""
menu in tkinter
1. add_cascade   -  create menu with different layers
2. add_command - assign command to menu button
3. add_separator  - create a separator for menubar

concept:
1. First have root as Tk(), this is the root layer for all elements
2. Second add Menu class to the root layer
3. Third add more submenu to the the root layer Menu class
4. add cascade and separator in order to create vivid looking and gain readability
"""
from tkinter import *


def callback():
    print("caled the menu")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=callback)
file_menu.add_command(label='Open...', command=callback)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=callback)

help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About...', command=callback)

root.mainloop()
