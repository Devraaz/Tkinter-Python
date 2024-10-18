import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tmsg


ROOT_WIDTH = 540
ROOT_HEIGHT = 420

root = ctk.CTk()
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")

# Frame1 goes here
frame1 = ctk.CTkFrame(root, corner_radius=10, width=400, height=400)
frame1.pack(ipadx=20, padx=20, pady=20, ipady=20, side="left",anchor="nw")

label1 = ctk.CTkLabel(frame1, text="Enter dimension to resize window")
label1.grid(padx=5, pady=5, row=0, column=1)

width = ctk.CTkLabel(frame1, text="Width: " )
width.grid(padx=5, pady=5, row=1, column=0)

width_input = ctk.CTkEntry(frame1)
width_input.grid(padx=5, pady=5, row=1, column=1)



height = ctk.CTkLabel(frame1, text="Height: " )
height.grid(padx=5, pady=5, row=2, column=0)

height_input = ctk.CTkEntry(frame1)
height_input.grid(padx=5, pady=5, row=2, column=1)

def change_dim(event):
    width = int(width_input.get())
    height = int(height_input.get())
    root.geometry(f"{width}x{height}")
    tmsg.showinfo("Info", "Sized changed Successfully")
    

button = ctk.CTkButton(frame1, text="Change Dimension")
button.grid(padx=5, pady=5, row=4, column=1)

button.bind("<ButtonRelease>", change_dim)


root.mainloop()

