import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tmsg

# Initialize the CustomTkinter app
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()  # CustomTkinter root window
root.geometry("400x400")
root.title("CustomTkinter with Menu Bar")

# Function to be called by menu items
def greet():
    print("Hello! You clicked a menu item.")


def help_box():
    print("Hey! I'll help you!")
    tmsg.showinfo("Help","Hey! I'll help you!")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label = "New Project", command=greet)
file_menu.add_command(label="Save", command=greet)
file_menu.add_command(label="Save As", command=greet)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label = "Undo", command=greet)
edit_menu.add_command(label="Redo", command=greet)

menu_bar.add_cascade(label="Edit", menu=edit_menu)




help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label = "Assistant", command=help_box)

menu_bar.add_cascade(label="Help", menu=help_menu)




root.config(menu=menu_bar)




# Run the application
root.mainloop()
