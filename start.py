from main import Application
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("330x150")
root.iconphoto(False, tk.PhotoImage(file='broom.png'))
root.title("Desktop Cleaner")
style = ttk.Style(root)
root.resizable(False, False)
myapp = Application(root)
myapp.mainloop()