from tkinter import *
import TKinterClasses as TKC

def calculate():
    """Berechnung der Werte"""

window = Tk()
window.title("Solarrechner [Niklas, Marco, Cilia, Sarah, Nico]")
window.geometry("600x400")

amountlabel = TKC.classLabel(window, None, "Menge Solarpanele:", 1, 3, 0, 0)
calculateButton = TKC.classButton(window, None,"berechnen", calculate, 1, 3, 0)

window.mainloop()