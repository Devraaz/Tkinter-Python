import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as msg
import sqlite3


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
    # Insert a new Contact into the database

    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO password (url, username, password) VALUES (?,?,?)", (url, username, password))

    conn.commit()
    cursor.close()
    msg.showinfo("Success", "Contact saved Successfully")

def fetch_password():
    # Fetch all the username and password

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

    if url =="" or username=="" or password == "":
        msg.showwarning("Input Error", "All Fields are Required")
    else:
        insert_password(url, username, password)
        display_password()


def display_password():
    pass_list.delete("1.0", tk.END)
    for row in fetch_password():
        pass_list.insert(tk.END, f"{row[1]} - {row[2]} - {row[3]} \n")
    pass_list.configure(state='disabled')  # Disable editing after inserting




root = ctk.CTk()
root.title("Password Saver")
root.geometry("500x600")

ctk.set_appearance_mode('dark')
current_mode = "dark"  # Track the current mode


def change_mode():
    global current_mode
    if current_mode == "dark":
        ctk.set_appearance_mode("light")
        mode_btn.configure(text="Switch to Dark Mode")  # Update button text
        current_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        mode_btn.configure(text="Switch to Light Mode")  # Update button text
        current_mode = "dark"


heading = ctk.CTkLabel(root, text="Password Saver", font=("", 20, "bold"))
heading.pack()


# =================
#   Frame 2 
# =================

frame1 = ctk.CTkFrame(root, corner_radius=10 )
frame1.pack(ipadx = 10, ipady = 10, padx=10, pady = 10, fill="x")

url_lb = ctk.CTkLabel(frame1, text="Website:").grid(row = 0,column = 0, padx=10, pady=10)
username_lb = ctk.CTkLabel(frame1, text="Username:").grid(row = 1,column = 0, padx=10, pady=10)
password_lb = ctk.CTkLabel(frame1, text="Password:").grid(row = 2,column = 0, padx=10, pady=10)

url_input = ctk.CTkEntry(frame1)
url_input.grid(row=0, column=1, padx=10, pady=10)
username_input = ctk.CTkEntry(frame1)
username_input.grid(row=1, column=1, padx=10, pady=10)
password_input = ctk.CTkEntry(frame1)
password_input.grid(row=2, column=1, padx=10, pady=10)

button = ctk.CTkButton(frame1, text="Submit", command=add_password)
button.grid(row=3, column=1)

mode_btn = ctk.CTkButton(master=frame1, text="Switch to Light Mode", command=change_mode,)
mode_btn.grid(row=0, column=2, padx=40)






# =================
#   Frame 2 
# =================

frame2 = ctk.CTkFrame(root, corner_radius=10 )
frame2.pack(ipadx = 10, ipady = 10, padx=10, pady = 10, fill="x")

pass_list = ctk.CTkTextbox(frame2, width=500, height=300)
pass_list.pack(pady=20, padx=20)


create_table()
display_password()


root.mainloop()