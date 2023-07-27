#hesap makinesi

from tkinter import*

pencere = Tk()
pencere.geometry("350x300")
pencere.title("CALCULATOR")
pencere.resizable(FALSE, FALSE)

def topla():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    lbl4['text'] = int(s1+s2)
def cıkar():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    lbl4['text'] = int(s1-s2)
def carp():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    lbl4['text'] = int(s1*s2)
def bol():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    lbl4['text'] = float(s1/s2)
def mod():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    lbl4['text'] = int(s1%s2)            


lbl1 = Label(text="Number1", font="Verdana 12 bold")
lbl1.place(x=20, y=20)
lbl2 = Label(text="Number 2", font="Verdana 12 bold")
lbl2.place(x=20, y=60)
lbl3 = Label(text="Result", font="Verdana 12 bold")
lbl3.place(x=20, y=100)
lbl4 = Label(font="Verdana 14 bold", bg="silver", width="13")
lbl4.place(x=140, y=100)

ent1 = Entry(font="Verdana 12 bold", fg="blue", width="15")
ent1.place(x=140, y=20)
ent2 = Entry(font="Verdana 12 bold", fg="blue", width="15")
ent2.place(x=140, y=60)

btn1 = Button(text=" + ", font="Verdana 12 bold", command=topla)
btn1.place(x=50, y=150)
btn2 = Button(text=" - ", font="Verdana 12 bold", command=cıkar)
btn2.place(x=200, y=150)
btn3 = Button(text="X ", font="Verdana 12 bold", command=carp)
btn3.place(x=50, y=200)
btn4 = Button(text=" /", font="Verdana 12 bold", command=bol)
btn4.place(x=200, y=200)
btn5 = Button(text="MOD", font="Verdana 12 bold", command=mod)
btn5.place(x=130, y=250)



pencere.mainloop()