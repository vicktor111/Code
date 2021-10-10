from tkinter import Tk, Button, Label, Entry, Widget

string = """#863200
#c8c8c8"""


class Config:

    def __init__(self, master, text: str, x, y, num, width=20):
        list_with_str = string.split("\n")
        Label(master, text=text).place(x=x, y=y - 2)
        self._text = Entry(master, width=width)
        self._text.insert(0, list_with_str[num])
        self._text.place(y=y, x=len(text) * 5 + 20 + x)

    def getinfo(self):
        info = self._text.get()
        if info[0] == "#" and len(info[1:len(info)]) == 6:
            return info
        else:
            return "#ffffff"

def save_info(info, funcname):
    with open("config", "w") as file:
        file.write(info)
        funcname(info.split("\n"))

def config(window, function):
    root = Tk()
    root.geometry("200x200")
    root.title("Настройки")
    Label(root, text="Настройки").pack()
    con_1 = Config(root, "Задній фон", 10, 20, 0, 10)
    con_2 = Config(root, "Колір кнопки", 10, 40, 1, 10)
    btn = Button(root, text="save",
                 command=lambda: save_info(f"{con_1.getinfo()}\n{con_2.getinfo()}",function))
    btn.place(x=30, y=90)

    root.mainloop()
