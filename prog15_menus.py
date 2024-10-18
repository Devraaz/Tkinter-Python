import tkinter as tk
import customtkinter as ctk

# Initialize the CustomTkinter app
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()  # CustomTkinter root window
root.geometry("400x400")
root.title("CustomTkinter with Menu Bar")

# Function to be called by menu items
def greet():
    print("Hello! You clicked a menu item.")


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











root.config(menu=menu_bar)
































# # Create the traditional Tkinter Menu bar
# yourmenubar = tk.Menu(root)

# # Create a 'File' menu
# file_menu = tk.Menu(yourmenubar, tearoff=0)
# file_menu.add_command(label="New Project", command=greet)
# file_menu.add_command(label="Save", command=greet)
# file_menu.add_separator()  # Adds a separator line
# file_menu.add_command(label="Save As", command=greet)
# file_menu.add_command(label="Exit", command=root.quit)

# # Add 'File' menu to the menu bar
# yourmenubar.add_cascade(label="File", menu=file_menu)

# # Create an 'Edit' menu
# edit_menu = tk.Menu(yourmenubar, tearoff=0)
# edit_menu.add_command(label="Undo", command=greet)
# edit_menu.add_command(label="Redo", command=greet)

# # Add 'Edit' menu to the menu bar
# yourmenubar.add_cascade(label="Edit", menu=edit_menu)

# # Create a 'Help' menu
# help_menu = tk.Menu(yourmenubar, tearoff=0)
# help_menu.add_command(label="About", command=greet)

# # Add 'Help' menu to the menu bar
# yourmenubar.add_cascade(label="Help", menu=help_menu)

# # Set the menu bar to the root window
# root.config(menu=yourmenubar)

# # Add some CustomTkinter widgets (optional)
# label = ctk.CTkLabel(root, text="CustomTkinter with Menu Bar Example", font=("Arial", 16))
# label.pack(pady=20)

# button = ctk.CTkButton(root, text="Click Me", command=greet)
# button.pack(pady=20)

# Run the application
root.mainloop()
