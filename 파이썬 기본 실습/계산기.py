from tkinter import *
def myFunc1():
    entry1.insert(END,"7")
def C():
    entry1.delete(0,END)
def myFunc2():
    entry1.insert(END,"8")
def myFunc3():
    entry1.insert(END,"9")
def myFunc4():
    entry1.insert(END,"/")
def myFunc5():
    entry1.insert(END,"4")
def myFunc6():
    entry1.insert(END,"5")
def myFunc7():
    entry1.insert(END,"6")
def myFunc8():
    entry1.insert(END,"*")
def myFunc9():
    entry1.insert(END,"1")
def myFunc10():
    entry1.insert(END,"2")
def myFunc11():
    entry1.insert(END,"3")
def myFunc12():
    entry1.insert(END,"-")
def myFunc13():
    entry1.insert(END,"0")
def myFunc14():
    entry1.insert(END,".")
def myFunc15():
    entry1.insert(END,"+")
def equal():
    result=eval(entry1.get())
    C()
    entry1.insert(0,result)
    
window=Tk()
entry1 = Entry(window, width=33, bg="yellow")
button1=Button(window, text="7", command=myFunc1,width=5)
button2=Button(window, text="8", command=myFunc2,width=5)
button3=Button(window, text="9", command=myFunc3,width=5)
button4=Button(window, text="/", command=myFunc4,width=5)
button5=Button(window, text="C", command=C,width=5)
button6=Button(window, text="4", command=myFunc5,width=5)
button7=Button(window, text="5", command=myFunc6,width=5)
button8=Button(window, text="6", command=myFunc7,width=5)
button9=Button(window, text="*", command=myFunc8,width=5)
button10=Button(window, text="", width=5)
button11=Button(window, text="1", command=myFunc9,width=5)
button12=Button(window, text="2", command=myFunc10,width=5)
button13=Button(window, text="3", command=myFunc11,width=5)
button14=Button(window, text="-", command=myFunc12,width=5)
button15=Button(window, text="",width=5)
button16=Button(window, text="0", command=myFunc13,width=5)
button17=Button(window, text=".", command=myFunc14,width=5)
button18=Button(window, text="=", command=equal,width=5)
button19=Button(window, text="+", command=myFunc15,width=5)
button20=Button(window, text="", width=5)

entry1.grid(row=0,column=0,columnspan=5)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=1,column=4)
button6.grid(row=2,column=0)
button7.grid(row=2,column=1)
button8.grid(row=2,column=2)
button9.grid(row=2,column=3)
button10.grid(row=2,column=4)
button11.grid(row=3,column=0)
button12.grid(row=3,column=1)
button13.grid(row=3,column=2)
button14.grid(row=3,column=3)
button15.grid(row=3,column=4)
button16.grid(row=4,column=0)
button17.grid(row=4,column=1)
button18.grid(row=4,column=2)
button19.grid(row=4,column=3)
button20.grid(row=4,column=4)

window.mainloop()
