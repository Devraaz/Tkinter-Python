import tkinter as tk


root = tk.Tk()
root.title("Driving Elegibility")
root.geometry("596x420")
root.minsize(420, 220)

# Label 
label0 = tk.Label(root, text="Program to find you are eligible to drive or not!", font=("", "18"), wraplength=500)
label0.pack(pady=10)

# Label 
label1 = tk.Label(root, text="Please enter your age: ")
label1.pack(pady=10)

#Entry
entry1 = tk.Entry(root, width=30 )
entry1.pack(pady=10)

def show_elegibility():
    try:
        age = int(entry1.get())
        if age > 18:
            output_label.config(text=f"As your age is {age}, You are eligible to drive")
        else:
            output_label.config(text=f"As your age is {age}, You are not eligible to drive")
    except Exception as e:
        output_label.config(text=f"Please enter properly")
# button
button1 = tk.Button(root, text="Enter", command=show_elegibility )
button1.pack(pady=10)


# Output
output_label = tk.Label(root, text="")
output_label.pack(pady=10)


root.mainloop()