import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x700")
root.maxsize(1200,700)
root.minsize(400,300)
root.title("News Paper Program")

image_files = ['img1.jpg', 'img2.jpg', 'img3.jpg']

photos = []


heading = tk.Label(root, text="MY NEWSPAPAER", font=("Sans", 20, "bold"), fg="darkgreen")
heading.pack(pady=20)

# This is the dynamic way to code the images 
for img_file in image_files:
    img = Image.open(img_file)
    img.thumbnail((300,300))

    photo = ImageTk.PhotoImage(img)
    photos.append(photo)

    label = tk.Label(root, image=photo)
    label.pack(pady=10)



# this is the manual way to code the images one by one

# img1 = Image.open('img1.jpg').resize((150,150))
# img2 = Image.open('img2.jpg')
# img3 = Image.open('img3.jpg')

# photo1 = ImageTk.PhotoImage(img1)
# photo2 = ImageTk.PhotoImage(img2)
# photo3 = ImageTk.PhotoImage(img3)


# tnail1 = tk.Label(image = photo1)
# tnail2 = tk.Label(image = photo2)
# tnail3 = tk.Label(image = photo3)


# tnail1.pack(pady=10)
# tnail2.pack(pady=10)
# tnail3.pack(pady=10)





root.mainloop()