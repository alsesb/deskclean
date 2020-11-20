import tkinter as tk
from tkinter import ttk
import desktopclearn
import webbrowser

class Application(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.d_cleaner = desktopclearn.DesktopCleaner() ## Creating a DesktopCleaner class.
        self.grid(padx = 5, pady = 20)
        self.create_widgets()

    def create_widgets(self):
        self.how_to = self.create_labels("Select the folder you want to clean and hit 'Start Foldering' !", 0, 0, 11, 55)
        self.path_text = self.create_texts(in_text = "No path selected yet!", row = 2, column = 1, columnspan = 6, width = 45)
        self.create_buttons("Select Path", self.select_and_refresh, 3, 1, 3)
        self.create_buttons("Start Foldering", self.doit_and_refresh, 3, 4, 3)
        self.attr_creator = self.create_labels("Icon created by Freepik!", 4, 0, 11, 25)
        self.attr_creator.bind("<Button-1>", lambda e: self.callback("https://www.flaticon.com/authors/freepik"))

    def callback(self, url):
        webbrowser.open_new(url)

    def refresh_entry_text(self):
        self.path_text.config(state = 'enabled')
        self.path_text.delete(0,'end')
        self.path_text.insert('insert', self.d_cleaner.get_path())
        self.path_text.config(state = 'disabled')

    def select_and_refresh(self):
        self.d_cleaner.select_path()
        self.refresh_entry_text()
    def doit_and_refresh(self):
        self.d_cleaner.clean_desktop()
        self.refresh_entry_text()

    def create_buttons(self, bt_text, command, row, column, columnspan):
        select_path = ttk.Button(self.master, text = bt_text, command = command)
        select_path.grid(row = row, column = column, columnspan = columnspan)

    def create_texts(self, in_text, row, column, columnspan, width):
        text = ttk.Entry(self.master, width = width)
        text.insert('insert', in_text)
        text.config(state = 'disabled')
        text.grid(row = row, column = column, columnspan = columnspan)
        return text
    
    def create_labels(self, lab_text, row, column, columnspan, width):
        label = ttk.Label(self.master, width = width, text = lab_text)
        label.grid(row = row, column = column, columnspan = columnspan, sticky = '', padx = 7)
        return label

