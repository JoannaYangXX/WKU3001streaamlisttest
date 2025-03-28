import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Program")

# Create label
label = tk.Label(
    root, 
    text="Hello, World!"
    )

# Lay out label
label.pack()

# Run forever!
root.mainloop()