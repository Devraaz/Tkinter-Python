import tkinter as tk

def slider_changed(value):
    print(f"Slider value: {value}")

root = tk.Tk()
root.geometry("400x200")

# Create a horizontal slider
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed)
slider.pack(pady=20)

# Create a vertical slider
vertical_slider = tk.Scale(root, from_=0, to=100, orient="vertical", command=slider_changed)
vertical_slider.pack(side="left", padx=20)

root.mainloop()
