from tkinter import Tk, Button, Label
class name_file: ...
class Print: ...
def interpreter(file: name_file)->Print:
    l=[a for a in file.split("\n")]
    print(l)
    lab=0
    but=0
    f=0
    g=0
    for i in l:
        if i[0:6]=="start;": #1
            window=Tk()
        if i[0:9]=="geometry:":
            i=i[10:len(i)+1]
            c=[i for i in i.split(",")]
            window.geometry(f"{c[0]}x{c[0][0:len(c[1])]}")
        if i[0:6]=="title:":
            i=i[7:len(i)+1]
            c=[i for i in i.split(",")]
            window.title(f"{c[0][0:len(c[0])-1]}")

        if i[0:4]=="end;": #2
            window.mainloop()

        if i[0:7]=="Button;": #3
            button=Button(window)
            button.pack()

        if i[0:6]=="Label;": #3
            label=Label(window, text="Text")
            label.pack()

        if i[0:7]=="Button{": #4
            button=Button(window)
            g=0
            f=1
            but=1

        if i[0:6]=="Label{": #4
            label=Label(window)
            g=0
            f=1
            lab=1

        if i[0:5]=="  bg:" and f==1: #5
            if but==1:
                button.config(bg=f"{i[6:len(i)+1]}",activebackground=f"{i[6:len(l)+1]}")
            if lab==1:
                label.config(bg=f"{i[6:len(i)+1]}")
            f=1

        if i[0:6]=="  wid:" and f==1: #6
            if but==1:
                button.config(width=f"{i[7:len(i)+1]}")
            if lab==1:
                label.config(width=f"{i[7:len(i)]+1}")
            f=1

        if i[0:7]=="  heig:" and f==1: #7
            if but==1:
                button.config(height=f"{i[8:len(i)+1]}")
            if lab==1:
                label.config(height=f"{i[8:len(i)+1]}")
            f=1

        if i[0:7]=="  text:" and f==1: #7
            if but==1:
                button.config(text=f"{i[8:len(i)+1]}")
            if lab==1:
                label.config(text=f"{i[8:len(i)+1]}")
            f=1

        if i[0:8]=="  place:" and f==1: #8
            x=i[9:len(i)+1]
            c=[i for i in x.split(",")]
            x=int(c[0])
            y=int(c[1])
            f=1
            g=1

        if i[0]=="}": #9
            if but==1:
                but=0
                if g==1:
                    button.place(x=x,y=y)
                else:
                    button.pack()
            if lab==1:
                lab=0
                if g==1:
                    label.place(x=x,y=y)
                else:
                    label.pack()
            f=0

f="""
start;
title: d;
geometry: 500,500;
Label{
  text: red
  bg: red
  heig: 5
  place: 20,20
}
Button{
  wid: 10
  bg: green
}
end;
"""

if __name__=="__main__":
    filename=input("")
    file=open(filename,"r",encoding="utf-8")
    file=file.read()
    interpreter(file)