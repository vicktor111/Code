from os import walk as __walk
from random import randint
try:
    from colorama import init as __init, Fore as __Fore
except ModuleNotFoundError:
    class __Fore:
        RED="red"
        YELLOW="yellow"
        GREEN="green"
        BLUE="blue"
        WHITE="white"
    def __init():...
__init()

def randoms(max,stop):
    if stop<=200:
        for t in range(1,stop+1):
            randomm=randint(1,max)
            print(__Fore.YELLOW,randomm)

def d1(function):
    def d2(*args,**kwargs):
        print(__Fore.RED)
        function(*args,**kwargs)
        print(__Fore.YELLOW)
        function(*args,**kwargs)
        print(__Fore.GREEN)
        function(*args,**kwargs)
        print(__Fore.BLUE)
        function(*args,**kwargs)
        print(__Fore.WHITE)
    return d2

class List:
    def new_list(self, len=9, type=int, max=9):
        s=''
        for e in range(1,len):
            randomm=str(randint(1,max))
            s=s+randomm+" "
        randomm=str(randint(1,max))
        s=s+randomm
        return [type(a) for a in s.split(" ")]
    
    def addition_1(self,list_1,list_2):
        "addition_1([a,b],[c,d])->[a+c,b+d]"
        f=len(list_1)
        string=''
        u=0
        while u!=f-1:
            text=list_1[u]+list_2[u]
            u=u+1
            string=string+str(text)+" "
        text2=list_1[u]+list_2[u]
        string=string+str(text2)
        return [int(s) for s in string.split(" ")]

    def subtraction_2(self,list_1,list_2):
        "subtraction_2([a,b],[c,d])->[a-c,b-d]"
        f=len(list_1)
        string=''
        u=0
        while u!=f-1:
            text=list_1[u]-list_2[u]
            u=u+1
            string=string+str(text)+" "
        text2=list_1[u]-list_2[u]
        string=string+str(text2)
        return [int(s) for s in string.split(" ")]

    def plural_3(self,list_1,list_2):
        "plural_3([a,b],[c,d])->[a*c,b*d]"
        f=len(list_1)
        string=''
        u=0
        while u!=f-1:
            text=list_1[u]*list_2[u]
            u=u+1
            string=string+str(text)+" "
        text2=list_1[u]*list_2[u]
        string=string+str(text2)
        return [int(s) for s in string.split(" ")]

    def division_4(self,list_1: list,list_2: list)->list:
        "division_4([a,b],[c,d])->[a/b,c/d]"
        f=len(list_1)
        string=''
        u=0
        while u!=f-1:
            text=list_1[u]/list_2[u]
            u=u+1
            string=string+str(text)+" "
        text2=list_1[u]/list_2[u]
        string=string+str(text2)
        return [float(s) for s in string.split(" ")]

def Locage(name,disk):
    "Функція для знаходження файлів в диску."
    s=0
    for dirpath, dirnames, filenames in __walk(f"{disk}:/"):
        for filename in filenames:
            if name==filename:
                s=int(1)
            if s==1:
                break
        if s==1:
            break
    return dirpath

def __r_g_b(n):
    f=0

    def new_func(n):
        if n==10:
            n="a"
        if n==11:
            n="b"
        if n==12:
            n="c"
        if n==13:
            n="d"
        if n==14:
            n="e"
        if n==15:
            n="f"
        return n

    while True:
        if n>15:
            n-=15
            n-=1
            f+=1
        else:
            break
    n=new_func(n)
    f=new_func(f)
    return f"{str(f)+str(n)}"

def rgb(r=0,g=0,b=0):
    "Функція яка перетворує rgb в hex."
    if r<=255 and g<=255 and b<=255:
        r=__r_g_b(r)
        g=__r_g_b(g)
        b=__r_g_b(b)
        return f"#{r}{g}{b}"

def rgb_2(n):
    "Функція яка перетворує hex в rgb."
    def new_func1(f):
            f=str(f)
            if f=="1":#1
                f=16
            if f=="2":#2
                f=32
            if f=="3":#3
                f=48
            if f=="4":#4
                f=64
            if f=="5":#5
                f=80
            if f=="6":#6
                f=96
            if f=="7":#7
                f=112
            if f=="8":#8
                f=128
            if f=="9":#9
                f=144
            if f=="a":#10
                f=160
            if f=="b":#11
                f=176
            if f=="c":#12
                f=192
            if f=="d":#13
                f=208
            if f=="e":#14
                f=224
            if f=="f":#15
                f=240
            return int(f)

    def new_func2(n):
        n=str(n)
        if n=="a":#1
            n=10
        if n=="b":#2
            n=11
        if n=="c":#3
            n=12
        if n=="d":#4
            n=13
        if n=="e":#5
            n=14
        if n=="f":#6
            n=15
        return int(n)

    f=str(n[1:7:2])
    n=str(n[2:7:2])
    a=[]
    for i in range(3):
        a+=[new_func1(f[i])+new_func2(n[i])]
    return a

def Color(color):
    import turtle
    turtle.title("Color.")
    turtle.setup(800,800)
    turtle.bgcolor(color)
    turtle.exitonclick()

def w(list):
    for i in range(len(list)):
        print(list[i])

if __name__=='__main__':
    input("hello")