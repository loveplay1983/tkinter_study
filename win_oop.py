from tkinter import *


class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.btn1 = Button(frame, text='Exit', fg='red',
                           command=frame.quit)
        self.btn1.pack()

        self.btn2 = Button(frame, text='Msg', fg='green',
                           command=self.say_hi)
        self.btn2.pack()

    def say_hi(self):
        print('Hello world')


root = Tk()
app = App(root)
root.mainloop()
root.destroy()
