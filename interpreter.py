from tkinter import Tk, Button, Label, Entry, Text
class name_file: ...
class Print: ...

def interpreter(file: name_file)->Print:

    def atribute_bg(wiget,index,code):
        if code.count("/")==1:
            code=[s for s in code.split("/")]
            wiget.config(bg=f"{code[0][index:len(code[0])-1]}")
        else:
            wiget.config(bg=f"{code[index:len(code)]}")
    
    def atribute_width(wiget,index,code):
        if code.count("/")==1: 
            code=[s for s in code.split("/")]
            wiget.config(width=f"{code[0][index:len(code[0])-1]}")
        else:
            wiget.config(width=f"{code[index:len(code)]}")

    def atribute_height(wiget,index,code):
        if code.count("/")==1:
            code=[s for s in code.split("/")]
            wiget.config(height=f"{code[0][index:len(code[0])-1]}")
        else:
            wiget.config(height=f"{code[index:len(code)]}")

    def atribute_text(wiget,index,code):
        if code.count("/")==1:
            code=[s for s in code.split("/")]
            wiget.config(text=f"{code[0][index:len(code[0])-1]}")
        else:
            wiget.config(text=f"{code[index:len(code)]}")

    def locage(wiget,value):
        if value==1:
            wiget.place(x=x,y=y)
        else:
            wiget.pack()

    list_with_code=[a for a in file.split("\n")]
    print(list_with_code)
    label_1=0
    button_1=0
    entry_1=0
    text_1=0

    for code in list_with_code:
        
        if code[0:len(code)]=="start;": #1.
            window=Tk()
            list_with_button=[]
            list_with_label=[]
            list_with_entry=[]
            list_with_text=[]
            n=1

        elif code[0:9]=="geometry:" and n==1: #2.
            code=code[10:len(code)+1]
            if code.count("/")==1:
                code=[i for i in code.split("/")]
                parameters=[i for i in code[0].split(",")]
            else:
                parameters=[i for i in code.split(",")]
            window.geometry(f"{parameters[0]}x{parameters[0][0:len(parameters[1])]}")

        elif code[0:7]=="script:" and n==1:
            code=code[8:len(code)+1]
            if code.count("/")==1:
                code=[i for i in code.split("/")]
                file=open(code[0][0:len(code[0])-2],'r',encoding='utf8')
                code_file=file.read()
                exec(code_file)
            else:
                file=open(code[0:len(code)-1],'r',encoding='utf8')
                code_file=file.read()
                exec(code_file)

        elif code[0:6]=="title:" and n==1:
            code=code[7:len(code)+1]
            if code.count("/")==1:
                code=[i for i in code.split("/")]
                window.title(f"{str(code[0])[0:len(code[0])-2]}")
            window.title(f"{code[0:len(code)-1]}")

        elif code[0:4]=="end;": #2.
            if n==1:
                window.mainloop()
                n=0
            else:
                raise SyntaxError(f"{code}")

        elif code[0:len(code)+1]=="Button{" and n==1: #3.
            button=Button(window)
            list_with_button.append(button)
            g=0
            f=1
            button_1=1

        elif code[0:len(code)+1]=="Label{" and n==1: #4.
            label=Label(window)
            list_with_label.append(label)
            g=0
            f=1
            label_1=1

        elif code[0:len(code)+1]=="Entry{" and n==1: #4.
            entry=Entry(window)
            g=0
            f=1
            entry_1=1

        elif code[0:len(code)+1]=="Text{" and n==1: #4.
            text=Text(window)
            g=0
            f=1
            text_1=1

        elif code[0:5]=="  bg:" and f==1: #5.
            if button_1==1:
                atribute_bg(button,6,code)
            if label_1==1:
                atribute_bg(label,6,code)
            if entry_1==1:
                atribute_bg(entry,6,code)
            if text_1==1:
                atribute_bg(text,6,code)
            f=1

        elif code[0:8]=="  width:" and f==1: #6.
            if button_1==1:
                atribute_width(button,9,code)
            if label_1==1:
                atribute_width(label,9,code)
            if entry_1==1:
                atribute_width(entry,9,code)
            if text_1==1:
                atribute_width(text,9,code)
            f=1

        elif code[0:9]=="  height:" and f==1: #7.
            if button_1==1:
                atribute_height(button,10,code)
            if label_1==1:
                atribute_height(label,10,code)
            if entry_1==1:
                atribute_height(entry,10,code)
            if text_1==1:
                atribute_height(text,10,code)
            f=1

        elif code[0:7]=="  text:" and f==1: #8.
            if button_1==1:
                atribute_text(button,8,code)
            if label_1==1:
                atribute_text(label,8,code)
            f=1

        elif code[0:8]=="  place:" and f==1: #14.
            i=code[9:len(code)+1]
            parameters=[i for i in i.split(",")]
            x=int(parameters[0])
            y=int(parameters[1])
            f=1
            g=1

        elif code[0:10]=="  command:": #15.
            exec(code_file)
            if button_1==1:
                parameter=code[11:len(code)+1]
                if code.count("/")==1:
                    parameter=[s for s in parameter.split("/")]
                    button.config(command=f"{parameter[0]}")
                else:
                    exec(f"button.config(command={parameter})")
            else:
                raise SyntaxError(f"{code}")
            f=1

        elif code=="}": #10.
            if button_1==1:
                locage(button,g)
                button_1=0
            if label_1==1:
                locage(label,g)
                label_1=0
            if entry_1==1:
                locage(entry,g)
                entry_1=0
            if text_1==1:
                locage(text,g)
                text_1=0
            f=0
        elif code=="": #11.
            pass
        elif code[0]=="/": #12.
            pass
        else:
            raise SyntaxError(f"{code}")

if __name__=="__main__":
    filename=input("Вкажіть файл ")
    file=open(filename,"r",encoding="utf-8")
    file=file.read()
    interpreter(file)