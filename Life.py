from tkinter import Tk, Button, Label # Модуль для створення графічного інтерфейса.
from PIL import Image, ImageDraw


a2=[]
but_2=[]
kk_2=[]
s=1
click=0
number_of_squares=0

class Life:

    def __init__(self): 
        self._x = 47 # Кількість кнопок по x.
        self._y = 31 # Кількість кнопок по y.

    def new_image(self):
        image=Image.new("RGB", (799, 844),"#ffffff")
        object=ImageDraw.Draw(image)
        for y in range(31):
            for x in range(47):
                if a2[y][x]==1 or kk_2[y][x]==1:
                    object.rectangle((x*17, y*27.226, (x+1)*17, (y+1)*27.226),fill="#835700",outline="#694100")
        image.show()

    def __pressing_on_green_button(self,s):
        global click
        click+=1 # Збільшення зміної click на 1.
        text_2["text"]=f"Зелену кнопку було нажато: {click}"
        if s<=15 and s>0:
            for i in range(1,s+1):
                self.__change_color_buttons()
        else:
            self.__change_color_buttons()

    def __tt(self):
        for a2_indexs in range(len(a2)):
            k=0
            for indexs in range(len(a2[a2_indexs])):
                k=0
                if indexs<len(a2[a2_indexs])-1: #1
                    if a2[a2_indexs][indexs+1]==1:
                        k+=1
                if indexs>1: #2
                    if a2[a2_indexs][indexs-1]==1:
                        k+=1
                if a2_indexs<len(a2)-1: #3
                    if a2[a2_indexs+1][indexs]==1:
                        k+=1
                if a2_indexs>1: #4
                    if a2[a2_indexs-1][indexs]==1:
                        k+=1
                if a2_indexs<len(a2)-1 and indexs>1: #5
                    if a2[a2_indexs+1][indexs-1]==1:
                        k+=1
                if a2_indexs<len(a2)-1 and indexs<len(a2[a2_indexs])-1: #6
                    if a2[a2_indexs+1][indexs+1]==1:
                        k+=1
                if a2_indexs>1 and indexs<len(a2[a2_indexs])-1: #7
                    if a2[a2_indexs-1][indexs+1]==1:
                        k+=1
                if a2_indexs>1 and a2_indexs>1: #8
                    if a2[a2_indexs-1][indexs-1]==1:
                        k+=1
                if k==2:
                    kk_2[a2_indexs][indexs]=1
                else:
                    kk_2[a2_indexs][indexs]=0

    def __change_color_buttons(self):
        s=[]
        global number_of_squares
        number_of_squares=0
        self.__tt()
        for kk_2_indexs in range(len(kk_2)):
            for indexs in range(len(kk_2[kk_2_indexs])):
                if kk_2[kk_2_indexs][indexs]==1:
                    but_2[kk_2_indexs][indexs]["bg"]="#000000" # Зміна кольору кнопки.
                    but_2[kk_2_indexs][indexs]["activebackground"]="#000000"
                    but_2[kk_2_indexs][indexs]["activeforeground"]="#c8c8c8"
                    but_2[kk_2_indexs][indexs]["text"]="1" # Зміна тексту кнопки.
                    but_2[kk_2_indexs][indexs]["fg"]="#c8c8c8" # Зміна кольору тексту кнопки.
                    a2[kk_2_indexs][indexs]=1
                    number_of_squares+=1 # Збільшення кількості квадратів.
                    text["text"]=f"Чорних квадратів: {number_of_squares}"
                else:
                    but_2[kk_2_indexs][indexs]["bg"]="#c8c8c8" # Зміна кольору кнопки.
                    but_2[kk_2_indexs][indexs]["activebackground"]="#c8c8c8"
                    but_2[kk_2_indexs][indexs]["activeforeground"]="#000000"
                    but_2[kk_2_indexs][indexs]["text"]="0" # Зміна тексту кнопки.
                    but_2[kk_2_indexs][indexs]["fg"]='#000000' # Зміна кольору тексту кнопки.
                    a2[kk_2_indexs][indexs]=0
            s+=a2[kk_2_indexs]
        if sum(s)==0:
            number_of_squares=0
            text["text"]=f"Чорних квадратів: {number_of_squares}"

    def __color_change(self,button,x,y): # Метод який виконується при нажимані кнопки.
        if button["bg"]=="#c8c8c8": # Якщо кнопка буде сірого кольору.
            global number_of_squares
            number_of_squares+=1 # Збільшення кількості квадратів.
            text["text"]=f"Чорних квадратів: {number_of_squares}"
            button["bg"]="#000000" # Зміна кольору кнопки.
            button["activeforeground"]="#c8c8c8"
            button["activebackground"]="#000000"
            button["text"]="1" # Зміна тексту кнопки.
            button["fg"]="#c8c8c8" # Зміна кольору тексту кнопки.
            a2[y][x]=1
        else:
            button["bg"]="#c8c8c8"
            button["activebackground"]="#c8c8c8"
            button["activeforeground"]="#000000"
            button["text"]="0"
            button["fg"]="#000000"
            a2[y][x]=0
            number_of_squares-=1 # Зминшення кількості квадратів.
            text["text"]=f"Чорних квадратів: {number_of_squares}"

    def __to_cleanse(self):
        global number_of_squares
        number_of_squares=0
        text["text"]="Чорних квадратів: 0"
        for indexs_1 in range(self._y):
            for indexs_2 in range(self._x):
                but_2[indexs_1][indexs_2]["bg"]="#c8c8c8" # Зміна кольору кнопки.
                but_2[indexs_1][indexs_2]["activebackground"]="#c8c8c8"
                but_2[indexs_1][indexs_2]["text"]="0" # Зміна тексту кнопки.
                but_2[indexs_1][indexs_2]["fg"]="#000000" # Зміна кольору тексту кнопки.
                a2[indexs_1][indexs_2]=0
                kk_2[indexs_1][indexs_2]=0

    def start_window(self): # Створення вікна з парамитрами.
        global window
        window=Tk() # Створення об'єкта вікно.
        window.title("Life")
        window.config(bg="#833200")

    def creation_of_buttons(self):
        global text, text_2
        window.geometry("799x844") # Розміри вікна.
        window.resizable(False,False) # Заборона на зміну розміра вікна.
        kk_1=[] # Пустий список.
        list_of_int=[]
        buttons=[]
        for y in range(self._y):
            for x in range(self._x):
                button_1=Button(window, text="0", width=1, height=1, bg="#c8c8c8", fg="#000000", activebackground="#c8c8c8", activeforeground="#000000") # Створення копки з парамитрами.
                button_1.config(command=lambda but=button_1, x=x, y=y: self.__color_change(but,x,y)) # Доповнені параметри для кнопки.
                kk_1.append(0) # Добавлення числа в список.
                buttons.append(button_1) # Добавлення кнопки в список.
                list_of_int.append(0) # Добавлення числа в список.
                button_1.grid(column=x, row=y) # Метод для розподілу кнопок.
            kk_2.append(kk_1) # Добавлення списка в інший список.
            but_2.append(buttons)
            a2.append(list_of_int)
            list_of_int=[] # Очищення списка.
            buttons=[]
            kk_1=[]
        Button(window, text="start", width=3, height=1, bg="#00aa00", command=lambda :self.__pressing_on_green_button(s)).place(x=20, y=811) # Створення зелиної копки з парамитрами.
        Button(window, text="to cleanse", width=7, height=1, bg="#aa0000", command=self.__to_cleanse).place(x=300, y=811) # Створення червоної копки з парамитрами.
        Button(window, text="s", width=3, height=1, bg="#0000aa", command=self.new_image).place(x=600,y=811)
        text=Label(text=f"Чорних квадратів: {number_of_squares}",fg="#dd8c5a" ,bg="#833200", font=1) # Створення текста з парамитрами.
        text.place(x=388,y=811) # Розміщення текса на вікні.
        text_2=Label(window, text=f"Зелену кнопку було нажато: {click}", bg="#833200", fg="#dd8c5a", font=15)
        text_2.place(x=60,y=811)
        window.mainloop() # Метод який недає закретись просто так вікну.

game=Life()
game.start_window()
game.creation_of_buttons()