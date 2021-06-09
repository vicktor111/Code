from tkinter import Tk, Button, Label
class name_file: ...
class Print: ...

def interpreter(file: name_file)->Print:

    def atribute_bg(wiget,value,index):
        if value==1:
            wiget.config(bg=f"{i[index:len(i)+1]}")
    
    def atribute_width(wiget,value,index):
        if value==1:
            wiget.config(width=f"{i[index:len(i)+1]}")

    def atribute_height(wiget,value,index):
        if value==1:
            wiget.config(height=f"{i[index:len(i)+1]}")

    def atribute_text(wiget,value,index):
        if value==1:
            wiget.config(text=f"{i[index:len(i)+1]}")

    def locage(wiget,value):
        if value==1:
            wiget.place(x=x,y=y)
        else:
            wiget.pack()

    list_with_code=[a for a in file.split("\n")]
    print(list_with_code)
    label_1=0
    button_1=0
    f=0
    g=0
    n=0
    for code in list_with_code:
        if code[0:6]=="start;": #1.
            window=Tk()
            n=1
        elif code[0:9]=="geometry:":
            i=code[10:len(code)+1]
            parameters=[i for i in i.split(",")]
            window.geometry(f"{parameters[0]}x{parameters[0][0:len(parameters[1])]}")
        elif code[0:6]=="title:":
            i=code[7:len(code)+1]
            parameter=[i for i in i.split(",")]
            window.title(f"{parameter[0][0:len(parameter[0])-1]}")

        elif code[0:4]=="end;": #2.
            if n==1:
                window.mainloop()
                n=0
                print(n)
            else:
                raise SyntaxError(f"{code}")

        elif code[0:7]=="Button{": #3.
            button=Button(window)
            g=0
            f=1
            button_1=1

        elif code[0:6]=="Label{": #4.
            label=Label(window)
            g=0
            f=1
            label_1=1

        elif code[0:5]=="  bg:" and f==1: #5.
            atribute_bg(button,button_1,6)
            atribute_bg(label,label_1,6)
            f=1

        elif code[0:6]=="  wid:" and f==1: #6.
            atribute_width(button,button_1,7)
            atribute_width(label,label_1,7)

        elif code[0:7]=="  heig:" and f==1: #7.
            atribute_height(button,button_1,8)
            atribute_height(button,button_1,8)
            f=1

        elif code[0:7]=="  text:" and f==1: #8.
            atribute_text(button,button_1,8)
            atribute_text(label,label_1,8)
            f=1

        elif code[0:8]=="  place:" and f==1: #9.
            i=code[9:len(i)+1]
            parameters=[i for i in i.split(",")]
            x=int(parameters[0])
            y=int(parameters[1])
            f=1
            g=1

        elif code=="}": #10.
            if button_1==1:
                locage(button,g)
                button_1=0    
            if label_1==1:
                locage(label,g)
                label_1=0
            f=0
        elif code=="":
            pass
        elif code[0]=="#":
            pass
        else:
            raise SyntaxError(f"{code}")

if __name__=="__main__":
    filename=input("")
    file=open(filename,"r",encoding="utf-8")
    file=file.read()
    interpreter(file)