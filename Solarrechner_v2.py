from tkinter import *
from PIL import ImageTk, Image

class classWidget:
    def __init__(self, screen, bd, row, column):
        self.screen = screen
        self.bd = bd
        self.row = row
        self.column = column

class classLabel(classWidget):
    def __init__(self, screen, text, bd, width, x, y):
        super().__init__(screen, bd, x, y)
        self.text = text
        self.width = width

        self.label = Label(self.screen, text=self.text)
        self.input = Entry(window, bd=self.bd, width=self.width)

        self.label.grid(row = self.row, column = self.column)
        self.input.grid(row = self.row, column = self.column)

class classButton(classWidget):
    def __init__(self, screen, text, func, bd, x, y):
        super().__init__(screen, bd, x, y)
        self.text = text
        self.func = func

        self.button = Button(self.screen, text = self.text, bd=self.bd, command=self.func)

        self.button.grid(row = self.row, column = self.column)

def calculate():
    """Berechnung der Werte"""

window = Tk()
window.title("Solarrechner [Niklas, Marco, Cilia, Sarah, Nico]")
window.geometry("400x400")

#------Background-------  
bg = PhotoImage(file = "Assets/Background_1.png")
canvas1 = Canvas(window, width = 400, height = 400)
canvas1.grid(row = 0, column = 0)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
#------Background-------

amountlabel = classLabel(window, "Menge Solarpanele:", 1, 3, 3, 0)
calculateButton = classButton(window, "berechnen", calculate, 1, 0, 0)

window.mainloop()