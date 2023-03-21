from tkinter import *
import TKinterClasses as TK

def calculate():
    """Berechnung der Werte"""

window = Tk()
window.title("Solarrechner [Niklas, Marco, Cilia, Sarah, Nico]")
window.geometry("600x400")

amountlabel = TK.classLabel(window, "Menge Solarpanele:", 1, 3, 0, 0)
calculateButton = TK.classButton(window,"berechnen", calculate, 1, 3, 0)

testImage = TK.classImage(window, "Test.png", 0, 3, 2)
window.mainloop()