import os
import shutil

class DesktopCleaner:
    def desktop_path_create(self):
        self.path = os.path.join(os.environ["HOMEPATH"], "Desktop")

    def create_custom_path(self, path):
        self.path = path

    def clean_desktop(self):
        if (self.path != None or self.path != ""):
            try:
                for element in os.listdir(self.path):
                    if "." in element:
                        filename, file_extension = os.path.splitext(os.path.basename(f'{self.path}/{element}'))
                        print(filename)
                        d_file = DesktopFile(filename, file_extension)
                        d_file.create_dir(self.path)
                        d_file.move_file(self.path)
            except:
                print("Path is not good, check if you have called the desktop_path_create function.\nOtherwise check if the custom created path is good.\n")


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


desktop_Clean = DesktopCleaner()
desktop_Clean.create_custom_path("lol")
##desktop_Clean.desktop_path_create()
desktop_Clean.clean_desktop()
