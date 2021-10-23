from tkinter import Tk, Button, Label, Entry, Frame, END
import main

string = """#863200
#c8c8c8
#000000"""


class Config:

    def __init__(self, master, text: str, x, y, num, width=20):
        frame = Frame(master, width=len(text) + width)
        Label(frame, text=text).grid(row=0, column=0)
        self._text = Entry(frame, width=width)
        self._text.insert(0, main.open_file()[num])
        self._text.grid(row=0, column=1)
        frame.place(x=x, y=y - 2)

    def getinfo(self):
        info = self._text.get()
        if info[0] == "#" and len(info[1:len(info)]) == 6:
            return info
        else:
            return "#ffffff"

def save_info(info, funcname):
    with open("config_2", "w") as file:
        file.write(info)
        funcname(info.split("\n"))

def set_info(info, list_with_configs):
    for i in range(len(info)):
        list_with_configs[i]._text.delete(0, END)
        list_with_configs[i]._text.insert(0, info[i])


def config(window, function):
    root = Tk()
    root.geometry("300x200")
    root.title("Настройки")
    # root.resizable(False, False)
    Label(root, text="Настройки").pack()
    con_1 = Config(root, "Задній фон", 10, 20, 0, 10)
    con_2 = Config(root, "Колір кнопки", 10, 40, 1, 10)
    con_3 = Config(root, "Колір кнопки після нажимання", 10, 60, 2, 10)
    btn = Button(root, text="зберегти",
                 command=lambda: save_info(f"{con_1.getinfo()}\n{con_2.getinfo()}\n{con_3.getinfo()}", function))
    btn_2 = Button(root, text="1",
                   command=lambda: set_info(string.split("\n"), [con_1, con_2, con_3]))
    btn.place(x=30, y=90)
    btn_2.place(x=110, y=90)
    root.mainloop()
