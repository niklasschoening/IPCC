from tkinter import *

size_y = 450
size_x = 900

class c_Label:
    def __init__(self, screen, name, text, bd, width, row, column):
        self.screen = screen
        self.name = name
        self.text = text
        self.bd = bd
        self.width = width
        self.row = row
        self.column = column

        self.label = Label(self.screen, text=self.text)
        self.input = Entry(window, bd=self.bd, width=self.width)

        self.label.grid(row=self.row, column=self.column)
        self.input.grid(row=self.row, column=self.column+1)

class c_Button:
    def __init__(self, screen, name, text, func, bd, width, row, column):
        self.screen = screen
        self.name = name
        self.text = text
        self.func = func
        self.bd = bd
        self.width = width
        self.row = row
        self.column = column

        

window = Tk()
window.geometry(f"{size_x}x{size_y}")

amount_label = c_Label(window, "amount", "Menge Solarpanele:", 5, 2, 0, 0)

window.mainloop()