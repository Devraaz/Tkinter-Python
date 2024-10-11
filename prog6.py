import tkinter as tk

root = tk.Tk()
root.title("Webokraft Solutions")
root.geometry("596x420")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)


# Create an Entry widget
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Function to display the entered text
def show_text():
    name = entry.get()  # Get the text from the Entry widget
    output_label.config(text=f"Hello, {name}!")

# Create a Button to trigger the action
button = tk.Button(root, text="Submit", command=show_text)
button.pack(pady=10)

# Create a Label to display the output
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()