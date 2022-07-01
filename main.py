from tkinter import *
from Application import Application

root = Tk()
root.config(background="#33CCFF")
app = Application(root)
root.state('zoomed')
root.geometry("1500x700+25+50")
app.mainloop()
