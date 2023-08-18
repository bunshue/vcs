# ch17_29.py
from tkinter import *
from PIL import Image, ImageTk
                                
root = Tk()
root.title("ch17_29")

img = Image.open("hung.jpg")
myPhoto = ImageTk.PhotoImage(img)

text = Text()
text.image_create(END,image=myPhoto)
text.insert(END,"\n")
text.insert(END,"洪錦魁年輕時留學美國拍攝於Chicago")
text.pack(fill=BOTH,expand=True)
    
root.mainloop()












