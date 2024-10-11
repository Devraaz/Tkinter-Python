from tkinter import *
from PIL import Image, ImageTk

root  = Tk()
root.title("The Silent Trader")

root.geometry("540x320")

# For jpg images
image = Image.open("img2.jpg")
photo = ImageTk.PhotoImage(image)


# photo = PhotoImage(file="img1.jpg")
tnail_img = Label(image = photo)
tnail_img.pack()


root.mainloop()