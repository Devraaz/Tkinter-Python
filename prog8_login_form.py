import tkinter as tk


root =  tk.Tk()
root.title("Login Form Field")
root.geometry("540x320")
root.minsize(440,320)


heading = tk.Label(root, text="Login", font=("calibre", 14, "bold"))
heading.pack(pady=2)

username = tk.Label(root, text="Username", font=("calibre"))
username.pack(pady=2)

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=2)

password = tk.Label(root, text="Password", font=("calibre"))
password.pack(pady=2)

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=2)

login_button = tk.Button(root, text="Login")
login_button.pack(pady=2)


root.mainloop()