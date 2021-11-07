from tkinter import filedialog


def open_file(filename="config_2"):
    try:
        with open(filename, "r+") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        pass

def save_file(*info):
    file_name = filedialog.asksaveasfilename()
    try:
        with open(f"{file_name}.game", "w") as file:
            file.write(f"{info[0]}\n{info[1]}\n{info[2]}")
    except FileNotFoundError:
        pass