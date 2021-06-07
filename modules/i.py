from turtle import color as _color, speed as _speed, exitonclick as stop# Графічний модуль.
from turtle import goto, setup, ht, dot, width, write# Графічний модуль.
import math# Математичний модуль.
from colorama import Fore as _Fore, init as __init# Модуль для надання тексту колір в терміналі.
__init()

class game:# Клас game.
    setup(800,1000)

    def __init__(self,code="-",text="-",ss="-"):# Конструктор класа.
        self.__f=0#
        self.__code=code# Параметир який приймає два значення.
        self.__text=text# Параметир який приймає два значення.
        self.x=0# Кордината х.
        self.y=0# Кордината у.
        self.ss=ss# Параметир який приймає два значення.

    def new_goto(self,x=0,y=0,speed=1,color="red",wid=0):# Функція для створення.

        def s(x,y):
            print(_Fore.GREEN,f"{math.sqrt( (x-self.x)^2+(y-self.y)^2 )}cm")# Вивединня в терміналі довжину в см.
            print(_Fore.WHITE)

        ht()# Макеровка черепахи.
        if self.__code=="+": 
            print(_Fore.YELLOW,f"({x};{y})")# Вивединня в терміналі кординати точки.
        _speed(speed)# Швидкість.
        _color(color)# Колір прямої і точок.
        if self.__f==0: 
            if self.__text=="+": 
                write("(0;0)")# Функція яка показує кординати в графічному шнтерфейсі.
        dot()# Функція для створення точки.
        width(wid)# Розмір лінії.
        if self.ss=="+":
            s(x,y)
        goto(x,y)# Лінія.
        dot()# Функція для створення точки.
        if self.__text=="+": 
            write(f"({x};{y})")# Функція яка показує кординати в графічному шнтерфейсі.
        self.__f=1
        self.x=x
        self.y=y