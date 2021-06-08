"""
Код для створення графічного вікна.
start - команда для створення вікна.
button - команда для створення кнопки на вікні.
bg - зніна кольору віджитів.
wid - зніна шерини віджита.
heig - зніна висоти віджита.
text - добавлення тексту.

Готове графічне вікно.
start;
geometry: 100,100;
button{
  bg: red
  place: 50,50
}
end;
"""
from tkinter import Tk, Button, Label, Entry
class name_file: ...

def interpreter(file: name_file)->print:
    l=[a for a in file.split("\n")]
    print(l)
    for i in l:
        if i[0:len(l)+1]=="start;": #1
            window=Tk()
        if i[0:9]=="geometry:":
            i=i[10:len(i)+1]
            c=[i for i in i.split(",")]
            window.geometry(f"{c[0]}x{c[0][0:len(c[1])]}")
        if i[0:6]=="title:":
            i=i[7:len(i)+1]
            c=[i for i in i.split(",")]
            window.title(f"{c[0][0:len(c[0])-1]}")

        if i[0:len(l)+1]=="end;": #2
            window.mainloop()
        if i[0:len(l)+1]=="button;": #3
            button=Button(window)
            button.pack()
        if i[0:len(l)+1]=="button{": #4
            button=Button(window)
            g=0
            f=1
        if i[0:5]=="  bg:" and f==1: #5
            button.config(bg=f"{i[6:len(l)]}",activebackground=f"{i[6:len(l)]}")
            f=1
        if i[0:6]=="  wid:" and f==1: #6
            button.config(width=f"{i[7:len(l)]}")
            f=1
        if i[0:7]=="  heig:" and f==1: #7
            button.config(height=f"{i[8:len(l)]}")
            f=1
        if i[0:7]=="  text:" and f==1: #7
            button.config(text=f"{i[8:len(l)]}")
            f=1

        if i[0:8]=="  place:" and f==1: #8
            x=i[9:len(i)+1]
            c=[i for i in x.split(",")]
            x=int(c[0])
            y=int(c[1])
            f=1
            g=1
        if i=="}": #9
            if g==1:
                button.place(x=x,y=y)
            else:
                button.pack()
            f=0

if __name__=="__main__":
    f=input("Вкажіть файл ")
    s=open(f,"r",encoding="utf-8")
    f=s.read()
    interpreter(f)