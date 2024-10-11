import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("796x540")
root.minsize(450,320)
root.title("Webokraft Solutions")


def button_clicked():
    print("Button is Clicked by user")



button1 = ttk.Button(root, text="Styled Button")
button1.pack()


button2 = tk.Button(text="Click Me", padx=15, pady=1, command=button_clicked, bg="lightblue", fg="purple",activebackground="white", 
                   activeforeground="white", cursor="hand2")
button2.pack(pady=10)
root.mainloop()
