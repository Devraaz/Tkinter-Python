import customtkinter as ctk
import tkinter as tk


root = ctk.CTk()
root.geometry("400x500")
root.title("New CTk")
# root._set_appearance_mode("light")


# Setting up Menu and Submenu
def greet():
    print("Hello")


yourmenubar = tk.Menu(root)

m1 = tk.Menu(yourmenubar, tearoff=0)
m1.add_command(label="New Project", command=greet)
m1.add_command(label="Save", command=greet)
m1.add_separator()
m1.add_command(label="Save As", command=greet)

root.config(menu=yourmenubar)

yourmenubar.add_cascade(label='File', menu=m1)








# Frame 1 goes here
# 
# 
frame1 = ctk.CTkFrame(root,  corner_radius=10)
frame1.pack(pady=10,padx=10, side="left", fill="y")


lb1 = ctk.CTkLabel(frame1, text="Enter Your Name:")
lb1.pack(pady=20,)

ent1 = ctk.CTkEntry(frame1)
ent1.pack(pady=10, padx=5)

def show_name(event):
    name = ent1.get()
    out_label.configure(text=f"Hii {name}")
    ent1.delete(0, 100)
    pass


# On moving mouse out of the input text it will trigger the event
ent1.bind("<Leave>", show_name)







# Frame 2 goes here
# 
# 
frame2 = ctk.CTkFrame(root, corner_radius=10)
frame2.pack(padx=10, pady=10, side="top", fill="x")

out_label = ctk.CTkLabel(frame2, text="Hii", font=("Verdana", 24))
out_label.pack(ipady=10, anchor="w", ipadx=10)


root.mainloop()