import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as msg
import sqlite3


# -------------------
# --Database Setup --
# -------------------

# Hardcoded credentials (you can use a database instead)
USERNAME = "admin"
PASSWORD = "passwordis#pass"


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

def update_password(id, url, username,  password):
    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE password set url = ?, username = ?, password = ? WHERE id = ?",(url, username, password, id) )
    conn.commit()
    conn.close()
    msg.showinfo("Success", "Password Updated Successfully")
    
def delete_password(id):
    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM password WHERE id == ?", (id,))
    conn.commit()
    conn.close()
    msg.showinfo("Success", "Password Deleted Successfully")
    

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
    pass_list.delete(0, tk.END)
    for row in fetch_password():
        pass_list.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
    # pass_list.configure(state='disabled')  # Disable editing after inserting

def on_listbox_select(event):
    # Populate entry filed with selected data
    try:
        selected = pass_list.get(pass_list.curselection())
        password_id, url, username, password = selected.split(" - ")
        
        url_input.delete(0, tk.END)
        url_input.insert(0, url)

        username_input.delete(0, tk.END)
        username_input.insert(0, username)

        password_input.delete(0, tk.END)
        password_input.insert(0, password)

        global selected_password_id
        selected_password_id = int(password_id)
    except :
        pass

def delete_selected_password():
    if selected_password_id is not None:
        delete_password(selected_password_id)
        display_password()
        clear_inputs()

def update_selected_password():
    if selected_password_id is not None:
        url = url_input.get()
        username = username_input.get()
        password = password_input.get()

        if url =="" or username=="" or password == "":
            msg.showwarning("Input Error", "All Fields are Required")
        else:
            update_password(selected_password_id, url, username, password)
            display_password()

def clear_inputs():
    url_input.delete(0, tk.END)
    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    global selected_password_id
    selected_password_id = None




# -------------------
# -- Login Window --
# -------------------

def open_password_app():
    login_window.withdraw()  # Close the login window
    open_main_app()  # Open the main app

def validate_login():
    user = username_input_login.get()
    pwd = password_input_login.get()

    password_input_login.delete(0, tk.END)
    if user == USERNAME and pwd == PASSWORD:
        open_password_app()
    else:
        msg.showerror("Login Failed", "Invalid username or password")

def open_main_app():
    # =================
    #   Tkinter UI
    # =================
    global url_input, username_input, password_input, pass_list, current_mode, selected_password_id

    root = ctk.CTk()
    root.title("Password Saver")
    root.geometry("500x600")
    # Set the window icon
    root.iconbitmap("logo10.ico") 


    ctk.set_appearance_mode('dark')
    current_mode = "dark"  # Track the current mode
    selected_password_id = None  # Global variable to track selected password ID

    # Function to handle logout
    def logout():
        root.destroy()  # Close the main app window
        login_window.deiconify()  # Show the login window again

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
    #   Frame 1
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

    button = ctk.CTkButton(frame1, text="Add Password", command=add_password)
    button.grid(row=3, column=0, padx=10)
    button = ctk.CTkButton(frame1, text="Update Password", command=update_selected_password)
    button.grid(row=3, column=1, padx=10)
    button = ctk.CTkButton(frame1, text="Delete Password", command=delete_selected_password)
    button.grid(row=3, column=2, padx=10)

    mode_btn = ctk.CTkButton(master=frame1, text="Switch to Light Mode", command=change_mode,)
    mode_btn.grid(row=0, column=2, padx=5)






    # =================
    #   Frame 2 
    # =================

    frame2 = ctk.CTkFrame(root, corner_radius=10 )
    frame2.pack(ipadx = 10, ipady = 10, padx=10, pady = 10, fill="x")

    pass_list = tk.Listbox(frame2, width=50)
    pass_list.pack(pady=20, padx=20)

    pass_list.bind("<<ListboxSelect>>", on_listbox_select)

    ctk.CTkButton(root, text="Clear Inputs", command=clear_inputs).pack(pady=10)

     # Add the Logout button
    logout_button = ctk.CTkButton(root, text="Logout", command=logout)
    logout_button.pack(pady=10)

    create_table()
    display_password()


    root.mainloop()


login_window = ctk.CTk()
login_window.title("password Saver | Login")
login_window.geometry("400x300")

login_window.iconbitmap("logo10.ico") 
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
