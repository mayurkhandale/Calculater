from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnclearDisplay():
    global operator
    operator=""
    text_Input.set("")
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

ca=Tk()
ca.title("Calculater")
operator=""
text_Input=StringVar()
txtdisplay=Entry(ca,font=('arial',20,'bold'),bd=25,textvariable=text_Input,
                 insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)
btn7=Button(ca,padx=19,bd=8,fg="black",font=('arial',20,'bold'),text="7", command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(ca,text="8",fg="black",padx=19,bd=8,font=('arial',20),command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(ca,text="9",fg="black",padx=19,bd=8,font=('arial',20),command=lambda:btnclick(9)).grid(row=1,column=2)
btnplus=Button(ca,text="+",fg="black",padx=19,bd=8,font=('arial',20),command=lambda:btnclick("+")).grid(row=1,column=3)
btn4=Button(ca,text="4",fg="black",padx=19,bd=8,font=('arial',20),command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(ca,text="5",fg="black",padx=19,bd=8,font=('arial',20),command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(ca,text="6",padx=19,bd=8,fg="black",font=('arial',20),command=lambda:btnclick(6)).grid(row=2,column=2)
btnminus=Button(ca,text="-",padx=19,bd=8,fg="black",font=('arial',20),command=lambda:btnclick("-")).grid(row=2,column=3)
btn1=Button(ca,text="1",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(ca,text="2",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(ca,text="3",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick(3)).grid(row=3,column=2)
btnmul=Button(ca,text="*",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick("*")).grid(row=3,column=3)
btnper=Button(text="0",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick(0)).grid(row=4,column=0)
btnclear=Button(ca,text="clear",padx=19,bg="powder blue",font=('arial',20),fg="black",bd=8,command=btnclearDisplay).grid(row=4,column=2)
btnequal=Button(text="=",padx=19,font=('arial',20),fg="black",bd=8,command=btnequal).grid(row=4,column=1)
btndiv=Button(text="/",padx=19,fg="black",bd=8,font=('arial',20),command=lambda:btnclick("/")).grid(row=4,column=3)

mainloop()
