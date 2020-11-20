import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class DesktopCleaner:
    def desktop_path_create(self):
        self.path = os.path.join(os.environ["HOMEPATH"], "Desktop")

    def create_custom_path(self, path):
        self.path = path

    def get_path(self):
        try:
            return self.path
        except:
            return "No path selected!"
        
    def select_path(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askdirectory()
        if file_path:
            self.path = file_path

    def clean_desktop(self):
        try:
            self.path
        except AttributeError:
            messagebox.showwarning("Error!", "No Path was selected!")
        else:
            try:
                for element in os.listdir(self.path):
                    if "." in element:
                        filename, file_extension = os.path.splitext(os.path.basename(f'{self.path}/{element}'))
                        d_file = DesktopFile(filename, file_extension)
                        d_file.create_dir(self.path)
                        d_file.move_file(self.path)
                del self.path
            except:
                messagebox.showwarning("Error!","Path is not good, check if you have called the desktop_path_create function.\nOtherwise check if the custom created path is good.\n")


class DesktopFile:
    def __init__(self, name, filetype):
        self.name = name
        self.filetype = filetype

    def __repr__(self):
        return f'{self.name}{self.filetype}'
    def create_dir(self, path):
        try:
            self.new_directory = self.filetype.split(".")[1]
            os.mkdir(f'{path}/{self.new_directory.upper()} Files')
        except:
            pass

    def move_file(self, path):
        if self.filetype != '':
            original_path = f'{path}/{self.name}{self.filetype}'
            new_path = f'{path}/{self.new_directory} Files/{self.name}{self.filetype}'
            shutil.move(original_path, new_path)

