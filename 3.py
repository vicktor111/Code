from tkinter import *
def fun(event):
    try:
        a=[int(i) for i in text.get("1.0", END).split(",")]
    except ValueError:
        pass
    try:
        maximum["text"]=f"Максимальний бал: {str(max(a))}"
        minimum["text"]=f"Мінімальний бал: {str(min(a))}"
        serednii["text"]=f"Середній бал: {str(round(sum(a)/len(a),1))}"
    except UnboundLocalError:
        pass
    n=0
    s=0
    d=0
    v=0
    try:
        for i in a:
            if i<=3:
                n=n+1
            elif i>3 and i<=6:
                s=s+1
            elif i>6 and i<=9:
                d=d+1
            else:
                v=v+1
    except UnboundLocalError:
        pass
    label1["text"]=f"Н  {n}"
    label2["text"]=f"С  {s}"
    label3["text"]=f"Д  {d}"
    label4["text"]=f"В  {v}"
bg="#7e4d00"
bg_1="#9a3e00"
Window=Tk()
Window.title("Аналіз оцінок.")
Window.geometry("500x210")
Window.resizable(False,False)
C=Canvas(Window,width=500,height=210,bg="#7e4d00")
C.pack()
C.create_rectangle(70,100,473,119,fill="#9a3e00")#Підлога
C.create_rectangle(90,95,111,109,fill="white")#Крейда
C.create_rectangle(0,188,500,210,fill="#6a4407")#Підставка
text=Text(Window,bg="green",fg="white",width=50,height=5,cursor="pencil")
text.place(x=70,y=20)
label1=Label(Window,text="H",bg=bg,cursor="left_ptr")
label1.place(x=4,y=20)
label2=Label(Window,text="C",bg=bg,cursor="left_ptr")
label2.place(x=4,y=40)
label3=Label(Window,text="Д",bg=bg,cursor="left_ptr")
label3.place(x=4,y=60)
label4=Label(Window,text="В",bg=bg,cursor="left_ptr")
label4.place(x=4,y=80)
maximum=Label(Window,text="",bg=bg_1,cursor="top_left_arrow")
maximum.place(x=4,y=120)
minimum=Label(Window,text="",bg=bg_1,cursor="top_left_arrow")
minimum.place(x=4,y=140)
serednii=Label(Window,text="",bg=bg_1,cursor="top_left_arrow")
serednii.place(x=4,y=160)
Label(Window,text="Видіть оцінки.",fg="yellow",font=50,bg=bg,cursor="circle").place(x=200,y=122)
Window.bind("<Button-1>",fun)
Window.mainloop()