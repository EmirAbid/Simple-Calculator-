from tkinter import * 
#------------Create-window -------
win= Tk()
win.title('Calculatrice')
win.minsize(320,600)
win.maxsize(320,600)
win.config(background='#474545')
win.iconbitmap('/Calculator/Calculator-icon.ico')
#--------Variable--------
x=StringVar()
exp=' '
#--------Function--------
def setnum(num):
    global exp
    exp= exp + str(num)
    x.set(exp)
def clear():
    global exp 
    exp = ' '
    x.set(exp)
def calculator():
    try: 
        global exp
        output= str(eval(exp))
        x.set(output)
    except: 
        x.set("Error")
        exp = " "
#--------Frames ---------
frame1=Frame(win,width=320,height=170,bg='#474545')
frame2=Frame(win,width=320,height=430,bg='#3A3A3A')
#--------affichage---------
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
#----------Creating Label------------
entry1=Entry(frame1,state=NORMAL,disabledbackground='#3A3A3A',fg='#DCDBDB',bd='0',width=320,font=('Courier','35'),justify=RIGHT,textvariable=x)
entry1.config(background='#3A3A3A')
entry1.pack(expand=YES)
#-------- Creating-Buttons----------
#-------- Num_Buttons --------------
Button(frame2,text='C',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=clear).grid(row=0,column=3)
Button(frame2,text='1',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('1')).grid(row=1,column=0)
Button(frame2,text='2',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('2')).grid(row=1,column=1)
Button(frame2,text='3',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('3')).grid(row=1,column=2)
Button(frame2,text='-',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('-')).grid(row=1,column=3)
Button(frame2,text='4',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('4')).grid(row=2,column=0)
Button(frame2,text='5',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('5')).grid(row=2,column=1)
Button(frame2,text='6',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('6')).grid(row=2,column=2)
Button(frame2,text='+',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('+')).grid(row=2,column=3)
Button(frame2,text='7',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('7')).grid(row=3,column=0)
Button(frame2,text='8',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('8')).grid(row=3,column=1)
Button(frame2,text='9',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('9')).grid(row=3,column=2)
Button(frame2,text='*',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('*')).grid(row=3,column=3)
Button(frame2,text='%',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('/')).grid(row=4,column=0)
Button(frame2,text='0',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('0')).grid(row=4,column=1)
Button(frame2,text='.',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=lambda: setnum('.')).grid(row=4,column=2)
Button(frame2,text='=',bg='#343434',activebackground='#858181',fg='#DCDBDB',activeforeground='#F2F2F2',justify=CENTER,bd='0',height=4,width=8,command=calculator).grid(row=4,column=3)
win.mainloop()