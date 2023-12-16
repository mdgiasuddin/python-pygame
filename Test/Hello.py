from  tkinter import*
def Sub_Name():
   Sub1=num1
   Sub1=Ent.get()
   print(Sub1)
win=Tk()
win.geometry('500x500')



num1=StringVar()

Ent=Entry(win,bd=2,width=5,insertwidth=1,textvariable=num1, font=('arial',18,'bold' ), justify=LEFT).pack(side=LEFT,anchor=NW)
butt=Button(win, text='OK', font=('arial',12,'bold'),command=Sub_Name).pack()


win.mainloop()

