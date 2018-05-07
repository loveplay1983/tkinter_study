from tkinter import *

button = Button(text='Xuanbutton', padx=10, pady=10)
button.config(cursor='gumby')
button.config(bd=8, relief=RAISED)
button.config(font=('Helvetica', 10, 'bold italic'))

button2 = Button(text='test', padx=1, pady=1, cursor='gumby', bd=1,
                 relief=RAISED, font=('Times', 20, 'bold'))

button.pack()
button2.pack()
button.mainloop()
