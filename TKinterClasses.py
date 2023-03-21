from tkinter import *
from PIL import ImageTk, Image
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
        self.input = Entry(self.screen, bd=self.bd, width=self.width)

        self.label.grid(row = self.row, column = self.column)
        self.input.grid(row = self.row, column = self.column+1)

class classButton(classWidget):
    def __init__(self, screen, text, func, bd, row, column):
        super().__init__(screen, bd, row, column)
        self.text = text
        self.func = func

        self.button = Button(self.screen, text = self.text, bd=self.bd, command=self.func)

        self.button.grid(row = self.row, column = self.column)

class classImage(classWidget):
    def __init__(self, screen, imagePath, bd, row, column):
        super().__init__(screen, bd, row, column)
        self.imagePath = imagePath

        self.image = Image.open(self.imagePath)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = Label(self.screen, image = self.photo)
        self.label.image = self.photo

        self.label.grid(row = self.row, column = self.column)