from tkinter import *

class Switch:
    def __init__(self, title = "Switch"):
        window1 = Tk()
        window1.title(title)

        frame1 = Frame(window1)
        frame1.pack()

        self.name1 = StringVar()
        self.name2 = StringVar()

        Label(frame1, text = "Name 1: ").grid(row = 1, column = 1)
        Label(frame1, text="Name 2: ").grid(row=2,column=1)

        Entry(frame1, textvariable = self.name1).grid(row=1, column=2)
        Entry(frame1, textvariable=self.name2).grid(row=2, column=2)

        Button(frame1, text = "Switch", command = self.processButton).grid(row=3,column=3)

        window1.mainloop()

    def processButton(self):
        temp = self.name1.get()
        self.name1.set(self.name2.get())
        self.name2.set(temp)

Switch()