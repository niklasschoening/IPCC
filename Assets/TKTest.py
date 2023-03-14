# Import module 
from tkinter import *
  
# Create object 
window = Tk()
  
# Adjust size 
window.geometry("400x400")
  
# Add image file
bg = PhotoImage(file = "Assets/Background_1.png")
  
# Create Canvas
canvas1 = Canvas(window, width = 400, height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
  

window.mainloop()