import tkinter
import tkinter.font

class MyGUI:
  def __init__(root):
    # Create the main window. 
    root.main_window = tkinter.Tk()
    # Create the Canvas widget.
    root.canvas = tkinter.Canvas(
        root.main_window, 
        width=300, 
        height=300
        )
    # Create a Font object.
    myfont = tkinter.font.Font(
        family='Helvetica', 
        size=18, 
        weight='bold'
        )
    # Display some text.
    root.canvas.create_text(
        100, 
        100, 
        text='Hello World', 
        font=myfont)
    # Pack the canvas. 
    root.canvas.pack()
    # Start the mainloop. 
    tkinter.mainloop()
# Create an instance of the MyGUI class. 
my_gui = MyGUI()
