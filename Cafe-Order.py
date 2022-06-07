from tkinter import *


class Cafe:
    def __init__(self, parent):
        Coffee_Frame = Frame(parent, width=200, height=500, bg="#e3cbb3")
        Coffee_Frame.grid(row=0, column=0, rowspan=15)
        Main_Frame = Frame(parent, width=400, height=500, bg="white")

        Main_Frame.grid(row=0, column=1, rowspan=15)


# main routine
if __name__ == "__main__":
    root = Tk()
    cafe = Cafe(root)
    root.mainloop()
