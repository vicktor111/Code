from tkinter import Entry, Tk, Button, Label, filedialog, Menu, Event, END, DISABLED
from PIL import Image, ImageDraw
import configs
import f


__all__ = [
    'Object_Button',
    'Game']
two_d_list = []
list_with_btn = []
k_2 = []
number = 1
num_of_click = 0
number_of_squares = 0
var_with_num = 0

def clear_of_menu(window):
    "Створення меню"
    menu = Menu(window, tearoff=1, background="#000000")
    menu_1 = Menu(window, tearoff=0)
    menu_1.add_command(label="Зберехти файл", command=lambda: f.save_file(two_d_list, number_of_squares, num_of_click))
    menu.add_cascade(label="Файл", menu=menu_1)
    menu_1.add_command(label='Вікрите файл', command=lambda:k())
    window.config(menu=menu)

def _event_1(event: Event, menu: Menu):
    menu.post(event.x_root, event.y_root)

def _event(info):
    window.config(bg=info[0])
    for i in range(len(two_d_list)):
        for i_2 in range(len(two_d_list[i])):
            if two_d_list[i][i_2] == 0:
                list_with_btn[i][i_2].config(bg=info[1])
            elif two_d_list[i][i_2] == 1:
                list_with_btn[i][i_2].config(bg=info[2])


class Object_Button():

    def __init__(self, state: str=""):
        self.state = state

    def k(self):
        global num_of_click
        info = f.open_file()
        list_with_info = f.open_file(filedialog.askopenfilename())
        exec(f"global list_with_num\nlist_with_num={list_with_info[0]}")
        for indexs in range(len(list_with_num)):
            for indexs_2 in range(len(list_with_num[indexs]) - 1):
                if list_with_num[indexs][indexs_2] == 1:
                    # Зміна кольору кнопки.
                    list_with_btn[indexs][indexs_2]["bg"] = info[2]
                    list_with_btn[indexs][indexs_2]["activebackground"] = info[2]
                    list_with_btn[indexs][indexs_2]["activeforeground"] = "#c8c8c8"
                    # Зміна тексту кнопки.
                    list_with_btn[indexs][indexs_2]["text"] = "1"
                    # Зміна кольору тексту кнопки.
                    list_with_btn[indexs][indexs_2]["fg"] = "#c8c8c8"
                    two_d_list[indexs][indexs_2] = 1
                else:
                    list_with_btn[indexs][indexs_2]["bg"] = info[1]
                    list_with_btn[indexs][indexs_2]["activebackground"] = info[1]
                    list_with_btn[indexs][indexs_2]["activeforeground"] = "#000000"
                    list_with_btn[indexs][indexs_2]["text"] = "0"
                    list_with_btn[indexs][indexs_2]["fg"] = "#000000"
                    two_d_list[indexs][indexs_2] = 0
        window.update()
        text_1["text"] = f"Чорних квадратів: {list_with_info[1]}"
        num_of_click = int(list_with_info[2])
        text_2["text"] = f"Зелену кнопку було нажато: {list_with_info[2]}"

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
        global var_with_num
        info = f.open_file()
        number = []
        global number_of_squares
        number_of_squares = 0
        self.tt()
        for k_2_indexs in range(len(k_2)):
            for indexs in range(len(k_2[k_2_indexs])):
                if k_2[k_2_indexs][indexs] == 1:
                    # Зміна кольору кнопки.
                    list_with_btn[k_2_indexs][indexs]["bg"] = info[2]
                    list_with_btn[k_2_indexs][indexs]["activebackground"] = info[2]
                    list_with_btn[k_2_indexs][indexs]["activeforeground"] = "#c8c8c8"
                    # Зміна тексту кнопки.
                    list_with_btn[k_2_indexs][indexs]["text"] = "1"
                    # Зміна кольору тексту кнопки.
                    list_with_btn[k_2_indexs][indexs]["fg"] = "#c8c8c8"
                    two_d_list[k_2_indexs][indexs] = 1
                    number_of_squares += 1  # Збільшення кількості квадратів.
                    text_1["text"] = f"Чорних квадратів: {number_of_squares}"
                else:
                    list_with_btn[k_2_indexs][indexs]["bg"] = info[1]
                    list_with_btn[k_2_indexs][indexs]["activebackground"] = info[1]
                    list_with_btn[k_2_indexs][indexs]["activeforeground"] = "#000000"
                    list_with_btn[k_2_indexs][indexs]["text"] = "0"
                    list_with_btn[k_2_indexs][indexs]["fg"] = "#000000"
                    two_d_list[k_2_indexs][indexs] = 0
            number += two_d_list[k_2_indexs]
        if sum(number) == 0:
            var_with_num=1
            number_of_squares = 0
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"
        window.update()

    def color_change(self, button, x, y):
        info = f.open_file()
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
        info = f.open_file()
        global number_of_squares
        number_of_squares = 0
        text_1["text"] = "Чорних квадратів: 0"
        for indexs_1 in range(game._y):
            for indexs_2 in range(game._x):
                # Зміна кольору кнопки.
                list_with_btn[indexs_1][indexs_2]["bg"] = info[1]
                list_with_btn[indexs_1][indexs_2]["activebackground"] = info[1]
                list_with_btn[indexs_1][indexs_2]["text"] = "0"  # Зміна тексту кнопки.
                # Зміна кольору тексту кнопки.
                list_with_btn[indexs_1][indexs_2]["fg"] = "#000000"
                two_d_list[indexs_1][indexs_2] = 0
                k_2[indexs_1][indexs_2] = 0


class Game:

    def __init__(self, x=47, y=31):
        self._x = x  # Кількість кнопок по x.
        self._y = y  # Кількість кнопок по y.

    def new_image(self, string="no"):
        "Створення і збереження картенки"
        image = Image.new("RGB", (int(17 *self._x) + 1, int(27.226 * self._y) + 1))
        draw = ImageDraw.Draw(image)
        for y in range(self._y):
            for x in range(self._x):
                if two_d_list[y][x] == 1 or k_2[y][x] == 1:
                    draw.rectangle(
                        (x * 17, y * 27.226, (x + 1) * 17, (y + 1) * 27.226), fill="#835700", outline="#694100")
                else:
                    draw.rectangle(
                        (x * 17, y * 27.226, (x + 1) * 17, (y + 1) * 27.226), fill="#ffffff", outline="#d8ecff")
        if string == "yes":
            file_name = filedialog.asksaveasfilename(
                filetypes=[("Файл \"JPG\"", "*.jpg")])
            image.save(f"{file_name}.jpg")
        else:
            image.show()

    def _pressing_on_green_button(self, num, object: Object_Button, buttons):

        def set_property_of_entry(str):
            second.delete(0, END)
            second.insert(0, str)

        def set(event):
            global var_with_num
            var_with_num = 1

        global num_of_click, var_with_num
        window.bind("<Button-3>", lambda event: ...)
        buttons[0].config(state = DISABLED)
        buttons[1].config(state = DISABLED)
        buttons[2].config(state = DISABLED)
        num_of_click += 1
        text_2["text"] = f"Зелену кнопку було нажато: {num_of_click}"
        var_with_num = 0
        if second.get() == "" or second.get() == "0":
            set_property_of_entry(30)
        else:
            try:
                int(second.get())
            except:
                set_property_of_entry(30)
        for i in range(int(second.get())):
            num_2 = int(second.get())
            set_property_of_entry(num_2 - 1)
            window.bind("<Return>", set)
            if var_with_num == 1:
                set_property_of_entry(0)
                break
            if num <= 15 and num > 0:
                for i in range(1, num + 1):
                    object.change_color_buttons()
            else:
                object.change_color_buttons()
        buttons[0].config(state = "normal")
        buttons[1].config(state = "normal")
        buttons[2].config(state = "normal")
        window.bind("<Button-3>", lambda event: _event_1(event, menu_1))

    def start(self):
        "Створення вікна з параметрами"
        global window, menu_1
        info = f.open_file()
        window = Tk()  # Створення об'єкта вікно.
        window.title("Game")
        window.iconbitmap(r"E:\New folder\programs\git\Code\946 (1).ico")
        window.config(bg=info[0])
        window.geometry("799x861")  # Розміри вікна.
        window.resizable(False, False)  # Заборона на зміну розміра вікна.
        menu_1 = Menu(window, tearoff=0)
        menu_1.add_command(label='очищення', background="#aa0000",
                       command=lambda: object_btn.to_cleanse(self))
        menu_1.add_command(label='нова картинка', background="#8d4f00",
                       command=lambda: self.new_image("yes"))
        
        window.bind("<Button-3>", lambda event: _event_1(event, menu_1))

    def creation_of_buttons(self, object_btn: Object_Button):
        'Розміщення віджетів.'
        global text_1, text_2, second
        info = f.open_file()
        k_1 = []
        list_with_number = []
        but_1 = []
        for y in range(self._y):
            for x in range(self._x):
                button_1 = Button(window, text="0", width=1, height=1, bg=info[1], fg="#000000",
                                  activebackground=info[1], activeforeground="#000000")  # Створення копки з парамитрами.
                # Доповнені параметри для кнопки.
                button_1.config(command=lambda button=button_1,
                                x=x, y=y: object_btn.color_change(button, x, y))
                k_1.append(0)
                but_1.append(button_1)
                list_with_number.append(0)
                button_1.grid(column=x, row=y)  # Метод для розподілу кнопок.
            k_2.append(k_1)
            list_with_btn.append(but_1)
            two_d_list.append(list_with_number)
            list_with_number = []
            but_1 = []
            k_1 = []
        btn_2 = Button(window, text="очищення",
                    width=9, height=1, bg="#aa0000", command=lambda: object_btn.to_cleanse(self))
        btn_2.place(x=300, y=811)  # Створення червоної копки з парамитрами.
        btn_3 = Button(window, text="нова картинка", width=12, height=1, bg="#8d4f00",
               command=lambda: self.new_image("yes"))
        btn_3.place(x=600, y=811)
        btn_1 = Button(window, text="старт", width=5,
                height=1, bg="#00aa00")
        btn_1.config(command=lambda: self._pressing_on_green_button(number, object_btn, [btn_1, btn_2, btn_3]))
        btn_1.place(x=20, y=811)  # Створення зеленої копки з парамитрами.
        # Створення текста з парамитрами.
        text_1 = Label(text=f"Чорних квадратів: {number_of_squares}",
                             fg="#dd8c5a", bg="#833200", font=1)
        text_1.place(x=388, y=811)  # Розміщення текса на вікні.
        text_2 = Label(window, text=f"Зелену кнопку було нажато: {num_of_click}",
                             bg="#833200", fg="#dd8c5a", font=15)
        text_2.place(x=68, y=811)
        second = Entry(window, justify="center", width=5)
        second.place(x=733, y=811)
        menu_1.add_command(label="старт", background="#007700",
                       command=lambda: self._pressing_on_green_button(number, object_btn, [btn_1, btn_2, btn_3]))
        menu_1.add_command(label='настройки', background="#5166af", command=lambda: configs.configs(window, _event))
        clear_of_menu(window)
        window.mainloop()  # Метод який недає закретись просто так вікну.

if __name__ == "__main__":
    game = Game()
    object_btn = Object_Button("*")
    game.start()
    game.creation_of_buttons(object_btn)
