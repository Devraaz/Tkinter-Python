import tkinter as tk


root = tk.Tk()

root.geometry("450x360")
root.title("Star Printing Program")
root.maxsize(1200,620)

heading = tk.Label(root, text="Start Printing Program", font=("calibre", 14, "bold"))
heading.pack()

text1 = tk.Label(root, text="Enter number to print star: \n")
text1.pack()


input1 = tk.Entry(root, width=30)
input1.pack()

def print_star():
    try:
        num = int(input1.get())
        result = ""
        print(num)
        for i in range(1, num+1):
            result += "*   " * i + "\n"
            output_label.config(text = result)
    except Exception as e:
        output_label.config(text=f"Please enter a Valid Number")


button1 = tk.Button(root, text="Click", command=print_star)
button1.pack()



output_label = tk.Label(root, text="")
output_label.pack()



root.mainloop()