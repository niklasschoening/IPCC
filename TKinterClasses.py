from tkinter import *
from PIL import ImageTk, Image

class classWidget:
    def __init__(self, screen, frame, bd, row, column):
        self.screen = screen
        self.frame = frame
        self.bd = bd
        self.row = row
        self.column = column

class classLabel(classWidget):
    def __init__(self, screen, frame, text, bd, width, x, y):
        super().__init__(screen, frame, bd, x, y)
        self.text = text
        self.width = width

        self.label = Label(self.screen, text=self.text)
        self.input = Entry(self.screen, bd=self.bd, width=self.width)

        self.label.grid(row = self.row, column = self.column)
        self.input.grid(row = self.row, column = self.column+1)

class classButton(classWidget):
    def __init__(self, screen, frame, text, func, bd, row, column):
        super().__init__(screen, frame, bd, row, column)
        self.text = text
        self.func = func

        self.button = Button(self.frame, text = self.text, bd=self.bd, command=self.func)

        self.button.grid(row = self.row, column = self.column)