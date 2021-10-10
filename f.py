from tkinter import Tk, Button, Label, Entry

string= """#863200"""


class Config:

    def __init__(self, master, text: str, x, y, width=20):
        list_with_str = string.split("\n")
        Label(master, text=text).place(x=x , y=y - 2)
        self._text = Entry(master, width=width)
        self._text.insert(0, list_with_str[0])
        self._text.place(y=y, x=len(text) * 5 + 20 + x)

    def getinfo(self):
        info = self._text.get()
        if info[0] == "#" and len(info[1:len(info)]) == 6:
            return info
        else:
            return "#ffffff"

def save_info(info, window, filename="config"):
    with open(filename, "w") as file:
        file.write(info)
        window.config(bg=info)
        window.update()

def window(window: Tk):
    root = Tk()
    root.geometry("200x200")
    root.title("Настройки")
    Label(root, text="Настройки").pack()
    con_1 = Config(root, "Задній фон", 10, 20, 10)
    con_2 = Config(root, "Колір кнопки", 10, 40, 10)
    btn = Button(root, text="save", 
        command=lambda: save_info(f"{con_1.getinfo()}\n{con_2.getinfo()}",window))
    btn.place(x=30, y=40)
    
    root.mainloop()

if __name__ == "__main__":
    window(Tk())