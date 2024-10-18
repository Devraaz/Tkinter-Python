from customtkinter import *
from tkinter import messagebox

# Initialize the main window
root = CTk()
root.geometry("400x500")
root.title("Signup Form")

# Set the appearance mode
set_appearance_mode("dark")  # You can set it to "dark" as well
current_mode = "dark"
# Title label for the form
title_label = CTkLabel(root, text="Signup Form", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Name entry
name_label = CTkLabel(root, text="Name:")
name_label.pack(pady=10)
name_entry = CTkEntry(root, width=300)
name_entry.pack()

# Email entry
email_label = CTkLabel(root, text="Email:")
email_label.pack(pady=10)
email_entry = CTkEntry(root, width=300)
email_entry.pack()

# Password entry
password_label = CTkLabel(root, text="Password:")
password_label.pack(pady=10)
password_entry = CTkEntry(root, show="*", width=300)
password_entry.pack()

# Confirm Password entry
confirm_password_label = CTkLabel(root, text="Confirm Password:")
confirm_password_label.pack(pady=10)
confirm_password_entry = CTkEntry(root, show="*", width=300)
confirm_password_entry.pack()

# Function to validate the signup form
def signup():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if name == "" or email == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        # Successful signup action (you can replace this with saving data, etc.)
        messagebox.showinfo("Success", "Signup Successful!")
        # Clear the fields after successful signup
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        confirm_password_entry.delete(0, END)

# Signup Button
signup_button = CTkButton(master=root, text="Sign Up", corner_radius=20, command=signup)
signup_button.pack(pady=30)





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
btn = CTkButton(master=root, text="Switch to Light Mode", corner_radius=20, command=change_mode )
btn.pack()


# Start the main loop
root.mainloop()
