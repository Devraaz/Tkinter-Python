import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3

# ------------------------------
# Database setup and functions
# ------------------------------
def create_table():
    """Create a table if not exists."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def insert_contact(name, phone):
    """Insert a new contact into the database."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Contact saved successfully!")

def fetch_contacts():
    """Fetch all contacts from the database."""
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

# ------------------------------
# Tkinter UI Setup
# ------------------------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        insert_contact(name, phone)
        display_contacts()

def display_contacts():
    contacts_list.delete(0, tk.END)
    for row in fetch_contacts():
        contacts_list.insert(tk.END, f"{row[1]} - {row[2]}")

# Create the main window
root = ctk.CTk()
root.title("Contact Book")
root.geometry("400x400")

# Create input fields
name_label = ctk.CTkLabel(root, text="Name")
name_label.pack(pady=5)

name_entry = ctk.CTkEntry(root)
name_entry.pack(pady=5)

phone_label = ctk.CTkLabel(root, text="Phone")
phone_label.pack(pady=5)

phone_entry = ctk.CTkEntry(root)
phone_entry.pack(pady=5)

# Create Add button
add_button = ctk.CTkButton(root, text="Add Contact", command=add_contact)
add_button.pack(pady=10)

# Create Listbox to display contacts
contacts_list = tk.Listbox(root, width=40, height=10)
contacts_list.pack(pady=20)

# Display existing contacts on startup
create_table()
display_contacts()

# Start the Tkinter main loop
root.mainloop()
