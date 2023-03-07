from tkinter import *

size_y = 450
size_x = 900

class classWidget:
    def __init__(self, screen, bd, row, column):
        self.screen = screen
        self.bd = bd
        self.row = row
        self.column = column

class classLabel(classWidget):
    def __init__(self, screen, text, bd, width, row, column):
        super().__init__(screen, bd, row, column)
        self.text = text
        self.width = width

        self.label = Label(self.screen, text=self.text)
        self.input = Entry(window, bd=self.bd, width=self.width)

        self.label.grid(row=self.row, column=self.column)
        self.input.grid(row=self.row, column=self.column+1)

class classButton(classWidget):
    def __init__(self, screen, text, func, bd, row, column):
        super().__init__(screen, bd, row, column)
        self.text = text
        self.func = func

        self.button = Button(self.screen, text = self.text, bd=self.bd, command=self.func)

        self.button.grid(row=self.row, column=self.column)

def setBackground(file):
    """Hintergrundbild setzen"""
    filename = PhotoImage(file = "Assets/Background_1.png")
    background_label = Label(image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

def calculate():
    """Berechnung der Werte"""   

window = Tk()
window.geometry(f"{size_x}x{size_y}")
window.title("Solarrechner [Niklas, Marco, Cilia, Sarah, Nico]")
window.minsize(600, 300)
setBackground(None)

amountlabel = classLabel(window, "Menge Solarpanele:", 2, 2, 0, 0)
calculateButton = classButton(window, "berechnen", calculate, 2, 1, 1)

window.mainloop()