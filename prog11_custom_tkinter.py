from customtkinter import *

root = CTk()
root.geometry("600x400")
root.maxsize(1200,700)
root.minsize(400,300)
root.title("Toggle Mode")

set_appearance_mode('dark')
current_mode = "dark"  # Track the current mode


def change_mode():
    global current_mode
    if current_mode == "dark":
        set_appearance_mode("light")
        btn.configure(text="Switch to Dark Mode")  # Update button text
        current_mode = "light"
    else:
        set_appearance_mode("dark")
        btn.configure(text="Switch to Light Mode")  # Update button text
        current_mode = "dark"


btn = CTkButton(master=root, text="Toggle", corner_radius=20, command=change_mode )
btn.place(relx=0.5, rely=0.5, anchor="center")


root.mainloop()