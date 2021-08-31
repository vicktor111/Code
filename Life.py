# import os
from tkinter import Tk, Button, Label, filedialog, Menu, Event
from PIL import Image, ImageDraw


two_d_list = []
but_2 = []
kk_2 = []
number = 1
num_of_click = 0
number_of_squares = 0

def event_1(event: Event, menu: Menu):
    menu.post(event.x_root, event.y_root)


class Object_Button():

    def tt(self):
        for a2_indexs in range(len(two_d_list)):
            num = 0
            for indexs in range(len(two_d_list[a2_indexs])):
                num = 0
                if indexs < len(two_d_list[a2_indexs])-1:
                    if two_d_list[a2_indexs][indexs + 1] == 1:
                        num += 1
                if indexs > 1:
                    if two_d_list[a2_indexs][indexs - 1] == 1:
                        num += 1
                if a2_indexs < len(two_d_list)-1:
                    if two_d_list[a2_indexs + 1][indexs] == 1:
                        num += 1
                if a2_indexs > 1:
                    if two_d_list[a2_indexs - 1][indexs] == 1:
                        num += 1
                if a2_indexs < len(two_d_list)-1 and indexs > 1:
                    if two_d_list[a2_indexs + 1][indexs - 1] == 1:
                        num += 1
                if a2_indexs < len(two_d_list)-1 and indexs < len(two_d_list[a2_indexs])-1:
                    if two_d_list[a2_indexs + 1][indexs + 1] == 1:
                        num += 1
                if a2_indexs > 1 and indexs < len(two_d_list[a2_indexs])-1:
                    if two_d_list[a2_indexs - 1][indexs + 1] == 1:
                        num += 1
                if a2_indexs > 1 and a2_indexs > 1:
                    if two_d_list[a2_indexs - 1][indexs - 1] == 1:
                        num += 1
                if num == 2:
                    kk_2[a2_indexs][indexs] = 1
                else:
                    kk_2[a2_indexs][indexs] = 0

    def change_color_buttons(self):
        number = []
        global number_of_squares
        number_of_squares = 0
        self.tt()
        for kk_2_indexs in range(len(kk_2)):
            for indexs in range(len(kk_2[kk_2_indexs])):
                if kk_2[kk_2_indexs][indexs] == 1:
                    # Зміна кольору кнопки.
                    but_2[kk_2_indexs][indexs]["bg"] = "#000000"
                    but_2[kk_2_indexs][indexs]["activebackground"] = "#000000"
                    but_2[kk_2_indexs][indexs]["activeforeground"] = "#c8c8c8"
                    # Зміна тексту кнопки.
                    but_2[kk_2_indexs][indexs]["text"] = "1"
                    # Зміна кольору тексту кнопки.
                    but_2[kk_2_indexs][indexs]["fg"] = "#c8c8c8"
                    two_d_list[kk_2_indexs][indexs] = 1
                    number_of_squares += 1  # Збільшення кількості квадратів.
                    text_1["text"] = f"Чорних квадратів: {number_of_squares}"
                else:
                    but_2[kk_2_indexs][indexs]["bg"] = "#c8c8c8"
                    but_2[kk_2_indexs][indexs]["activebackground"] = "#c8c8c8"
                    but_2[kk_2_indexs][indexs]["activeforeground"] = "#000000"
                    but_2[kk_2_indexs][indexs]["text"] = "0"
                    but_2[kk_2_indexs][indexs]["fg"] = '#000000'
                    two_d_list[kk_2_indexs][indexs] = 0
            number += two_d_list[kk_2_indexs]
        if sum(number) == 0:
            number_of_squares = 0
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"

    def color_change(self, button, x, y):
        if button["bg"] == "#c8c8c8":  # Якщо кнопка буде сірого кольору.
            global number_of_squares
            number_of_squares += 1  # Збільшення кількості квадратів.
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"
            button["bg"] = "#000000"  # Зміна кольору кнопки.
            button["activeforeground"] = "#c8c8c8"
            button["activebackground"] = "#000000"
            button["text"] = "1"  # Зміна тексту кнопки.
            button["fg"] = "#c8c8c8"  # Зміна кольору тексту кнопки.
            two_d_list[y][x] = 1
        else:
            button["bg"] = "#c8c8c8"
            button["activebackground"] = "#c8c8c8"
            button["activeforeground"] = "#000000"
            button["text"] = "0"
            button["fg"] = "#000000"
            two_d_list[y][x] = 0
            number_of_squares -= 1  # Зминшення кількості квадратів.
            text_1["text"] = f"Чорних квадратів: {number_of_squares}"

    def to_cleanse(self, game):
        global number_of_squares
        number_of_squares = 0
        text_1["text"] = "Чорних квадратів: 0"
        for indexs_1 in range(game._y):
            for indexs_2 in range(game._x):
                # Зміна кольору кнопки.
                but_2[indexs_1][indexs_2]["bg"] = "#c8c8c8"
                but_2[indexs_1][indexs_2]["activebackground"] = "#c8c8c8"
                but_2[indexs_1][indexs_2]["text"] = "0"  # Зміна тексту кнопки.
                # Зміна кольору тексту кнопки.
                but_2[indexs_1][indexs_2]["fg"] = "#000000"
                two_d_list[indexs_1][indexs_2] = 0
                kk_2[indexs_1][indexs_2] = 0


class Game:

    def __init__(self, x=47, y=31):
        self._x = x  # Кількість кнопок по x.
        self._y = y  # Кількість кнопок по y.

    def new_image(self, string="no"):
        image = Image.new("RGB", (int(17 *self._x) + 1, int(27.226 * self._y) + 1))
        object = ImageDraw.Draw(image)
        for y in range(self._y):
            for x in range(self._x):
                if two_d_list[y][x] == 1 or kk_2[y][x] == 1:
                    object.rectangle(
                        (x * 17, y * 27.226, (x+1) * 17, (y+1) * 27.226), fill="#835700", outline="#694100")
                else:
                    object.rectangle(
                        (x * 17, y * 27.226, (x+1) * 17, (y+1) * 27.226), fill="#ffffff", outline="#d8ecff")
        if string == "yes":
            file_name = filedialog.asksaveasfilename(
                filetypes=[("Файл \"JPG\"", "*.jpg")])
            image.save(f"{file_name}.jpg")
        else:
            image.show()

    def __pressing_on_green_button(self, num, object: Object_Button):
        global num_of_click
        num_of_click += 1
        text_2["text"] = f"Зелену кнопку було нажато: {num_of_click}"
        if num <= 15 and num > 0:
            for i in range(1, num + 1):
                object.change_color_buttons()
        else:
            object.change_color_buttons()

    def start_window(self):
        global window
        window = Tk()  # Створення об'єкта вікно.
        window.title("Life")
        window.config(bg="#833200")
        menu_1 = Menu(window, tearoff=0)
        menu_1.add_command(label='Очестети поле', background="#aa0000",
                       command=lambda: btn.to_cleanse(self))
        menu_1.add_command(label='Зберехти картинку', background="#8d4f00",
                       command=lambda: self.new_image("yes"))
        window.bind("<Button-3>", lambda event: event_1(event, menu_1))

    def creation_of_buttons(self):
        global text_1, text_2
        window.geometry("799x844")  # Розміри вікна.
        window.resizable(False, False)  # Заборона на зміну розміра вікна.
        kk_1 = []
        list_with_number = []
        buttons = []
        for y in range(self._y):
            for x in range(self._x):
                button_1 = Button(window, text="0", width=1, height=1, bg="#c8c8c8", fg="#000000",
                                  activebackground="#c8c8c8", activeforeground="#000000")  # Створення копки з парамитрами.
                # Доповнені параметри для кнопки.
                button_1.config(command=lambda button=button_1,
                                x=x, y=y: btn.color_change(button, x, y))
                kk_1.append(0)
                buttons.append(button_1)
                list_with_number.append(0)
                button_1.grid(column=x, row=y)  # Метод для розподілу кнопок.
            kk_2.append(kk_1)
            but_2.append(buttons)
            two_d_list.append(list_with_number)
            list_with_number = []
            buttons = []
            kk_1 = []
        Button(window, text="start", width=3, 
                height=1, bg="#00aa00", command=lambda: self.__pressing_on_green_button(number, btn)).place(x=20, y=811)  # Створення зеленої копки з парамитрами.
        Button(window, text="to cleanse",
                    width=7, height=1, bg="#aa0000", command=lambda button_1=button_1 : btn.to_cleanse(self)).place(x=300, y=811)  # Створення червоної копки з парамитрами.
        Button(window, text="new image", width=8, height=1, bg="#8d4f00",
               command=lambda: self.new_image("yes")).place(x=600, y=811)
        # Створення текста з парамитрами.
        text_1 = Label(text=f"Чорних квадратів: {number_of_squares}",
                             fg="#dd8c5a", bg="#833200", font=1)
        text_1.place(x=388, y=811)  # Розміщення текса на вікні.
        text_2 = Label(window, text=f"Зелену кнопку було нажато: {num_of_click}",
                             bg="#833200", fg="#dd8c5a", font=15)
        text_2.place(x=60, y=811)
        window.mainloop()  # Метод який недає закретись просто так вікну.


game = Game()
btn = Object_Button()
game.start_window()
game.creation_of_buttons()
