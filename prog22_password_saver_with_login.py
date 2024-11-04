import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as msg
import sqlite3

# Hardcoded credentials (you can use a database instead)
USERNAME = "admin"
PASSWORD = "password123"

# -------------------
# --Database Setup --
# -------------------

def create_table():
    """Create a table if not exist"""
    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            url TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_password(url, username, password):
    """Insert a new password entry into the database"""
    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO password (url, username, password) VALUES (?,?,?)", (url, username, password))
    conn.commit()
    conn.close()
    msg.showinfo("Success", "Password saved successfully")

def fetch_password():
    """Fetch all the username and password"""
    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM password")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------------
# ---Tkinter UI--
# ---------------

def add_password():
    url = url_input.get()
    username = username_input.get()
    password = password_input.get()
    if url == "" or username == "" or password == "":
        msg.showwarning("Input Error", "All Fields are Required")
    else:
        insert_password(url, username, password)
        display_password()

def display_password():
    pass_list.configure(state='normal')  # Allow editing
    pass_list.delete("1.0", tk.END)  # Clear the textbox
    for row in fetch_password():
        pass_list.insert(tk.END, f"{row[1]} - {row[2]} - {row[3]}\n")
    pass_list.configure(state='disabled')  # Disable editing

# -------------------
# -- Login Window --
# -------------------

def open_password_app():
    login_window.withdraw()  # Close the login window
    open_main_app()  # Open the main app

def validate_login():
    user = username_input_login.get()
    pwd = password_input_login.get()

    if user == USERNAME and pwd == PASSWORD:
        open_password_app()
    else:
        msg.showerror("Login Failed", "Invalid username or password")

def open_main_app():
    global url_input, username_input, password_input, pass_list
    root = ctk.CTk()
    root.title("Password Saver")
    root.geometry("600x400")
    ctk.set_appearance_mode('dark')

    heading = ctk.CTkLabel(root, text="Password Saver", font=("", 20, "bold"))
    heading.pack()

    # Frame 1: Input
    frame1 = ctk.CTkFrame(root, corner_radius=10)
    frame1.pack(ipadx=10, ipady=10, padx=10, pady=10, fill="x")

    ctk.CTkLabel(frame1, text="Website:").grid(row=0, column=0, padx=10, pady=10)
    ctk.CTkLabel(frame1, text="Username:").grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkLabel(frame1, text="Password:").grid(row=2, column=0, padx=10, pady=10)

    url_input = ctk.CTkEntry(frame1)
    url_input.grid(row=0, column=1, padx=10, pady=10)
    username_input = ctk.CTkEntry(frame1)
    username_input.grid(row=1, column=1, padx=10, pady=10)
    password_input = ctk.CTkEntry(frame1)
    password_input.grid(row=2, column=1, padx=10, pady=10)

    ctk.CTkButton(frame1, text="Submit", command=add_password).grid(row=3, column=1)

    # Frame 2: Password List
    frame2 = ctk.CTkFrame(root, corner_radius=10)
    frame2.pack(ipadx=10, ipady=10, padx=10, pady=10, fill="x")

    pass_list = ctk.CTkTextbox(frame2, height=200, width=400)
    pass_list.pack(pady=20, padx=20)

    create_table()  # Ensure the table exists
    display_password()

    root.mainloop()

# -------------------
# -- Login UI --
# -------------------

login_window = ctk.CTk()
login_window.title("Login")
login_window.geometry("400x300")

ctk.set_appearance_mode('dark')

login_label = ctk.CTkLabel(login_window, text="Login", font=("", 20, "bold"))
login_label.pack(pady=20)

frame_login = ctk.CTkFrame(login_window, corner_radius=10)
frame_login.pack(ipadx=10, ipady=10, padx=10, pady=10, fill="x")

ctk.CTkLabel(frame_login, text="Username:").grid(row=0, column=0, padx=10, pady=10)
ctk.CTkLabel(frame_login, text="Password:").grid(row=1, column=0, padx=10, pady=10)

username_input_login = ctk.CTkEntry(frame_login)
username_input_login.grid(row=0, column=1, padx=10, pady=10)

password_input_login = ctk.CTkEntry(frame_login, show="*")
password_input_login.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(frame_login, text="Login", command=validate_login).grid(row=2, column=1, pady=20)

login_window.mainloop()
