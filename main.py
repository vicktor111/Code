from tkinter import Entry, Tk, Button, Label, filedialog, Menu, Event, END
from PIL import Image, ImageDraw
import config

two_d_list = []
but_2 = []
k_2 = []
number = 1
num_of_click = 0
number_of_squares = 0
g = 0

def open_file(filename="config_2"):
    with open(filename, "r+") as file:
        return file.read().split("\n")

def event_1(event: Event, menu: Menu):
    menu.post(event.x_root, event.y_root)

def event(info):
    window.config(bg=info[0])
    for i in range(len(two_d_list)):
        for i_2 in range(len(two_d_list[i])):
            if two_d_list[i][i_2] == 0:
                but_2[i][i_2].config(bg=info[1])
            elif two_d_list[i][i_2] == 1:
                but_2[i][i_2].config(bg=info[2])


class Object_Button():

    def __init__(self,state=""):
        self.state = state

    def tt(self):
        for a2_indexs in range(len(two_d_list)):
            num = 0
            for indexs in range(len(two_d_list[a2_indexs])):
                num = 0
                if indexs < len(two_d_list[a2_indexs]) - 1:
                    if two_d_list[a2_indexs][indexs + 1] == 1:
                        num += 1
                if indexs > 1:
                    if two_d_list[a2_indexs][indexs - 1] == 1:
                        num += 1
                if a2_indexs < len(two_d_list) - 1:
                    if two_d_list[a2_indexs + 1][indexs] == 1:
                        num += 1
                if a2_indexs > 1:
                    if two_d_list[a2_indexs - 1][indexs] == 1:
                        num += 1
                if a2_indexs < len(two_d_list) - 1 and indexs > 1:
                    if two_d_list[a2_indexs + 1][indexs - 1] == 1:
                        num += 1
                if a2_indexs < len(two_d_list) - 1 and indexs < len(two_d_list[a2_indexs]) - 1:
                    if two_d_list[a2_indexs + 1][indexs + 1] == 1:
                        num += 1
                if a2_indexs > 1 and indexs < len(two_d_list[a2_indexs]) - 1:
                    if two_d_list[a2_indexs - 1][indexs + 1] == 1:
                        num += 1
                if a2_indexs > 1 and a2_indexs > 1:
                    if two_d_list[a2_indexs - 1][indexs - 1] == 1:
                        num += 1
                if self.state == "*":
                    if two_d_list[a2_indexs][indexs] == 0:
                        if num == 3:
                            k_2[a2_indexs][indexs] = 1
                        else:
                            k_2[a2_indexs][indexs] = 0
                    elif two_d_list[a2_indexs][indexs] == 1:
                        if num == 3 or num == 2:
                            k_2[a2_indexs][indexs] = 1
                        else:
                            k_2[a2_indexs][indexs] = 0
                elif self.state == "":
                    if num == 2:
                        k_2[a2_indexs][indexs] = 1
                    else:
                        k_2[a2_indexs][indexs] = 0

    def change_color_buttons(self):
        global g
        info = open_file()
        number = []
        global number_of_squares
        number_of_squares = 0
        self.tt()
        for k_2_indexs in range(len(k_2)):
            for indexs in range(len(k_2[k_2_indexs])):
                if k_2[k_2_indexs][indexs] == 1:
                    # Зміна кольору кнопки.
                    but_2[k_2_indexs][indexs]["bg"] = info[2]
                    but_2[k_2_indexs][indexs]["activebackground"] = info[2]
                    but_2[k_2_indexs][indexs]["activeforeground"] = "#c8c8c8"
                    # Зміна тексту кнопки.
                    but_2[k_2_indexs][indexs]["text"] = "1"
                    # Зміна кольору тексту кнопки.
                    but_2[k_2_indexs][indexs]["fg"] = "#c8c8c8"
                    two_d_list[k_2_indexs][indexs] = 1
                    number_of_squares += 1  # Збільшення кількості квадратів.
                    text_1["text"] = f"Чорних квадратів: {number_of_squares}"
                else:
                    but_2[k_2_indexs][indexs]["bg"] = info[1]
                    but_2[k_2_indexs][indexs]["activebackground"] = info[1]
                    but_2[k_2_indexs][indexs]["activeforeground"] = "#000000"
                    but_2[k_2_indexs][indexs]["text"] = "0"
                    but_2[k_2_indexs][indexs]["fg"] = "#000000"
                    two_d_list[k_2_indexs][indexs] = 0
            number += two_d_list[k_2_indexs]
        if sum(number) == 0:
            g=1
            number_of_squares = 0
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"
        window.update()

    def color_change(self, button, x, y):
        info = open_file()
        if button["bg"] == info[1]:  # Якщо кнопка буде сірого кольору.
            global number_of_squares
            number_of_squares += 1  # Збільшення кількості квадратів.
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"
            button["bg"] = info[2]  # Зміна кольору кнопки.
            button["activeforeground"] = "#c8c8c8"
            button["activebackground"] = info[2]
            button["text"] = "1"  # Зміна тексту кнопки.
            button["fg"] = "#c8c8c8"  # Зміна кольору тексту кнопки.
            two_d_list[y][x] = 1
        else:
            button["bg"] = info[1]
            button["activebackground"] = info[1]
            button["activeforeground"] = "#000000"
            button["text"] = "0"
            button["fg"] = "#000000"
            two_d_list[y][x] = 0
            number_of_squares -= 1  # Зминшення кількості квадратів.
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"

    def to_cleanse(self, game):
        info = open_file()
        global number_of_squares
        number_of_squares = 0
        text_1["text"] = "Чорних квадратів: 0"
        for indexs_1 in range(game._y):
            for indexs_2 in range(game._x):
                # Зміна кольору кнопки.
                but_2[indexs_1][indexs_2]["bg"] = info[1]
                but_2[indexs_1][indexs_2]["activebackground"] = info[1]
                but_2[indexs_1][indexs_2]["text"] = "0"  # Зміна тексту кнопки.
                # Зміна кольору тексту кнопки.
                but_2[indexs_1][indexs_2]["fg"] = "#000000"
                two_d_list[indexs_1][indexs_2] = 0
                k_2[indexs_1][indexs_2] = 0


class Game:

    def __init__(self, x=47, y=31):
        self._x = x  # Кількість кнопок по x.
        self._y = y  # Кількість кнопок по y.

    def new_image(self, string="no"):
        image = Image.new("RGB", (int(17 *self._x) + 1, int(27.226 * self._y) + 1))
        object = ImageDraw.Draw(image)
        for y in range(self._y):
            for x in range(self._x):
                if two_d_list[y][x] == 1 or k_2[y][x] == 1:
                    object.rectangle(
                        (x * 17, y * 27.226, (x + 1) * 17, (y + 1) * 27.226), fill="#835700", outline="#694100")
                else:
                    object.rectangle(
                        (x * 17, y * 27.226, (x + 1) * 17, (y + 1) * 27.226), fill="#ffffff", outline="#d8ecff")
        if string == "yes":
            file_name = filedialog.asksaveasfilename(
                filetypes=[("Файл \"JPG\"", "*.jpg")])
            image.save(f"{file_name}.jpg")
        else:
            image.show()

    def _pressing_on_green_button(self, num, object: Object_Button):

        def set_property_of_entry(str):
            second.delete(0, END)
            second.insert(0, str)

        def set(event):
            global g
            g = 1

        global num_of_click, g
        num_of_click += 1
        text_2["text"] = f"Зелену кнопку було нажато: {num_of_click}"
        g=0
        if second.get() == "":
            set_property_of_entry(30)
        else:
            try:
                int(second.get())
            except :
                set_property_of_entry(30)
        for i in range(int(second.get())):
            num_2 = int(second.get())
            set_property_of_entry(num_2 - 1)
            window.bind("<Return>", set)
            if g == 1:
                set_property_of_entry(0)
                break
            if num <= 15 and num > 0:
                for i in range(1, num + 1):
                    object.change_color_buttons()
            else:
                object.change_color_buttons()

    def start(self):
        global window, menu_1
        info = open_file()
        window = Tk()  # Створення об'єкта вікно.
        window.title("Life")
        window.iconbitmap(r"E:\New folder\programs\git\Code\icons80.ico")
        window.config(bg=info[0])
        window.geometry("799x844")  # Розміри вікна.
        # window.resizable(False, False)  # Заборона на зміну розміра вікна.
        menu_1 = Menu(window, tearoff=0)
        menu_1.add_command(label='очищення', background="#aa0000",
                       command=lambda: btn.to_cleanse(self))
        menu_1.add_command(label='нова картинка', background="#8d4f00",
                       command=lambda: self.new_image("yes"))
        
        window.bind("<Button-3>", lambda event: event_1(event, menu_1))

    def creation_of_buttons(self):
        global text_1, text_2, second
        info = open_file()
        k_1 = []
        list_with_number = []
        but_1 = []
        for y in range(self._y):
            for x in range(self._x):
                button_1 = Button(window, text="0", width=1, height=1, bg=info[1], fg="#000000",
                                  activebackground=info[1], activeforeground="#000000")  # Створення копки з парамитрами.
                # Доповнені параметри для кнопки.
                button_1.config(command=lambda button=button_1,
                                x=x, y=y: btn.color_change(button, x, y))
                k_1.append(0)
                but_1.append(button_1)
                list_with_number.append(0)
                button_1.grid(column=x, row=y)  # Метод для розподілу кнопок.
            k_2.append(k_1)
            but_2.append(but_1)
            two_d_list.append(list_with_number)
            list_with_number = []
            but_1 = []
            k_1 = []
        Button(window, text="старт", width=5,
                height=1, bg="#00aa00", command=lambda: self._pressing_on_green_button(number, btn)).place(x=20, y=811)  # Створення зеленої копки з парамитрами.
        Button(window, text="очищення",
                    width=9, height=1, bg="#aa0000", command=lambda: btn.to_cleanse(self)).place(x=300, y=811)  # Створення червоної копки з парамитрами.
        Button(window, text="нова картинка", width=12, height=1, bg="#8d4f00",
               command=lambda: self.new_image("yes")).place(x=600, y=811)
        # Створення текста з парамитрами.
        text_1 = Label(text=f"Чорних квадратів: {number_of_squares}",
                             fg="#dd8c5a", bg="#833200", font=1)
        text_1.place(x=388, y=811)  # Розміщення текса на вікні.
        text_2 = Label(window, text=f"Зелену кнопку було нажато: {num_of_click}",
                             bg="#833200", fg="#dd8c5a", font=15)
        text_2.place(x=68, y=811)
        second = Entry(window, width=5)
        second.place(x=733, y=811)
        menu_1.add_command(label="старт", background="#007700",
                       command=lambda: self._pressing_on_green_button(number, btn))
        menu_1.add_command(label='настройки', background="#5166af", command=lambda: config.config(window, event))
        window.mainloop()  # Метод який недає закретись просто так вікну.

if __name__ == "__main__":
    game = Game()
    btn = Object_Button("*")
    game.start()
    game.creation_of_buttons()