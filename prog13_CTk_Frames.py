import customtkinter as ctk
import tkinter as tk


root = ctk.CTk()
root.geometry("400x500")
root.title("New CTk")
# root._set_appearance_mode("light")


frame1 = ctk.CTkFrame(root,  corner_radius=10)
frame1.pack(pady=10,padx=10, side="left", fill="y")


lb1 = ctk.CTkLabel(frame1, text="Enter Your Name:")
lb1.pack(pady=20,)

ent1 = ctk.CTkEntry(frame1)
ent1.pack(pady=10, padx=5)

def show_name():
    name = ent1.get()
    out_label.configure(text=f"Hii {name}")
    ent1.delete(0, 100)
    pass




btn1 = ctk.CTkButton(frame1, text="Click", command=show_name)
btn1.pack()


frame2 = ctk.CTkFrame(root, corner_radius=10)
frame2.pack(padx=10, pady=10, side="top", fill="x")

out_label = ctk.CTkLabel(frame2, text="Hii", font=("Verdana", 24))
out_label.pack(ipady=10, anchor="w", ipadx=10)


root.mainloop()