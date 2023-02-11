from tkinter import *

size_y = 110
size_x = 260

def calc():
    amount = amount_label.var.get()
    print(f"Output: {amount}")

def reset():
    print('Reset')

class c_Button:
    def __init__(self, screen, text, row, column, anchor, function):
        self.screen = screen
        self.text = text
        self.row = row
        self.column = column
        self.anchor = anchor
        self.command = function

        self.button = Button(self.screen, text = self.text, command=self.command)

        self.button.grid(row = self.row, column = self.column, sticky = self.anchor)

class c_Label:
    def __init__(self, screen, name, text, bd, width, row, column, anchor):
        self.screen = screen
        self.name = name
        self.text = text
        self.bd = bd
        self.width = width
        self.row = row
        self.column = column
        self.anchor = anchor

        self.var = StringVar()

        self.label = Label(self.screen, text=self.text, anchor=self.anchor)
        self.input = Entry(window, bd=self.bd, width=self.width, textvariable = self.var)

        self.label.grid(row=self.row, column=self.column, sticky= self.anchor)
        self.input.grid(row=self.row, column=self.column+1, sticky=self.anchor)

        self.output = self.var.get()
        print(f"output: {self.output}")

window = Tk()
window.geometry(f"{size_x}x{size_y}")

amount_label = c_Label(window, "amount", "Menge Solarpanele:", 0, 6, 0, 0, 'w')
kwp_label = c_Label(window, "kwP", "Welchen kwP produziert die Anlage?", 0, 6, 1, 0, 'w')
price_label = c_Label(window, "price", "Was kostet die Anlage?", 0, 6, 2, 0, 'w')

calc_b = c_Button(window, "Berechnen", 3, 0, 'w', calc)
reset_b = c_Button(window, "Reset", 3, 1, 'w', reset)

window.mainloop()