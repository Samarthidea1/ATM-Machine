import sqlite3
from sqlite3 import *
from Tkinter import *
from tkMessageBox import *

con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("create table if not exists atm(id number,name varchar2(15),pin number,balance number)")
def fun(a,b,c):
    a1=a.get()
    b1=b.get()
    c1=c.get()
    a2=(a1,b1,c1,0)
    cur.execute("insert into atm values(?,?,?,?)",a2)
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0,END)
    con.commit()
    showinfo('Created','Account Created \n Thanks for visiting')
    loginL()
def fun2():
    cur.execute("select * from atm ")
    print cur.fetchall()
def fun1():
    cur.execute("select * from atm where id=(?)",(d.get(),))
    print cur.fetchall()
                               

def entry():
    root1=Tk()
    root1.title('SIGN UP')
    root1.geometry('450x350')
    about6=PhotoImage(file='6.gif')
    Label(root1,image=about6).place(x=0,y=0,relwidth=1,relheight=1)
    Label(root1,text="Enter Account Number :",font='Ariel 10 ',fg='black').place(x=44,y=155)
    a=Entry(root1,border=4)
    a.place(x=193,y=152)
    Label(root1,text="Enter Name :",font='Ariel 10 ',fg='black').place(x=106,y=178)
    b=Entry(root1,border=4)
    b.place(x=193,y=177)

    Label(root1,text="Enter PIN :",font='Ariel 10 ',fg='black').place(x=120,y=202)
    c=Entry(root1,border=4)
    c.place(x=193,y=200)


    Button(root1,text="Submit",font='Ariel 10 bold',fg='black',command=lambda:[fun(a,b,c)]).place(x=210,y=235)
    root1.mainloop()

def loginL():
    login=Toplevel()
    login.title('LOGIN')
    login.geometry('450x350')
    about3=PhotoImage(file='3.gif')
    Label(login,image=about3).place(x=0,y=0,relwidth=1,relheight=1)
    Label(login,text='Account No. ',font='Ariel 10 bold',fg='black').place(x=5,y=130)
    acc=Entry(login)
    acc.place(x=92,y=131)
    Label(login,text='PIN ',font='Ariel 10 bold',fg='black').place(x=5,y=153)
    pasw=Entry(login)
    pasw.place(x=92,y=153)
    Button(login,text='Login',font='Ariel 10 bold',fg='black',command=lambda:[welcome(acc.get(),pasw.get(),login)]).place(x=125,y=175)
    login.mainloop()
    

def welcome(x,y,login):
    login.withdraw()
    cur.execute("select pin from atm where id="+x)
    z=cur.fetchone()
    print z[0]
    print y
    if int(y)==int(z[0]):
        
        depwith(x)
    else:
        showerror('Invalid','Incorrect Account Number or Passeord')
        login.deiconify()
    
def get_bal(x,e):
    cur.execute('select balance from atm where id='+x)
  
    showinfo("Balance", e)

    cur.execute('update atm set balance=balance+'+e+' where id='+x)
    con.commit()
    cur.execute('select balance from atm where id='+x)
    showinfo("Current Balance", cur.fetchone())

        

def get_bal1(x,e):
    cur.execute('select balance from atm where id='+x)
  
    showinfo("Balance", e)

    cur.execute('update atm set balance=balance-'+e+' where id='+x)
    con.commit()
    cur.execute('select balance from atm where id='+x)
    showinfo("Current Balance", cur.fetchone())
    
def depwith(x):
    dep=Toplevel()
    dep.title('DEPOSIT\WITHDRAWL')
    dep.geometry('450x350')
    about4=PhotoImage(file='4.gif')
    Label(dep,image=about4).place(x=0,y=0,relwidth=1,relheight=1)

    Button(dep,text='Deposit',width=14,font='Ariel 10 bold',fg='black',command=lambda:depo(x,dep)).place(x=10,y=320)
    Button(dep,text='Withdrawl',width=10,font='Ariel 10 bold',fg='black',command=lambda:withd(x,dep)).place(x=350,y=320)
    dep.mainloop()

def depo(a,dep):
    dep.destroy()
    de=Toplevel()
    de.title('DEPOSIT')
    de.geometry('450x350')
    about5=PhotoImage(file='5.gif')
    Label(de,image=about5).place(x=0,y=0,relwidth=1,relheight=1)
    Label(de,text='Amount ',width=14,font='Ariel 10 bold',fg='black').place(x=101,y=145)
    e=Entry(de)
    e.place(x=224,y=146)
    Button(de,text='Deposit',width=14,font='Ariel 10 bold',fg='black',command=lambda:[get_bal(a,e.get()),de.destroy()]).place(x=170,y=172)
    de.mainloop()

def withd(x,dep):
    dep.destroy()
    wit=Toplevel()
    wit.title('WITHDRAWL')
    wit.geometry('450x350')
    about6=PhotoImage(file='5.gif')
    Label(wit,image=about6).place(x=0,y=0,relwidth=1,relheight=1)
    Label(wit,text='Amount ',width=14,font='Ariel 10 bold',fg='black').place(x=101,y=145)
    e=Entry(wit)
    e.place(x=224,y=146)
    Button(wit,text='Withdraw',width=14,font='Ariel 10 bold',fg='black',command=lambda:[get_bal1(x,e.get()),wit.destroy()]).place(x=170,y=172)
    Label(wit,text='Your current balance: ')
    wit.mainloop()


def first(main):
    main.destroy()
    fir=Tk()
    fir.title('ATM')
    about2=PhotoImage(file='2.gif')
    fir.geometry('504x450')
    Label(fir,image=about2).place(x=0,y=0)
    Label(fir,text='Welcome to Apna ATM',justify=LEFT).grid(row=0,column=0)
    Button(fir,text="Create a new Account",width=20,font='Ariel 10 bold',fg='black',command=lambda:[fir.destroy(),entry()]).place(x=100,y=415)
    Button(fir,text="Login",width=10,font='Ariel 10 bold',fg='black',command=lambda:[fir.destroy(),loginL()]).place(x=330,y=415)
    #Button(fir,text="Withdrawal",command=fun2).grid(row=5,column=2)
    fir.mainloop()

def mains():
    main=Tk()
    about1=PhotoImage(file='1.gif')
    main.geometry('1200x600')
    main.title('Intro')
   
    Label(main,image=about1,bg='blue').place(x=0,y=0)
    Label(main,text='Name').place(x=7,y=10)
    Label(main,text='ATM Project',font='Chiller 20').place(x=8,y=8)
    Button(main,text='Enter',width=10,font='Ariel 10 bold',fg='black',command=lambda:[first(main)]).place(x=205,y=415)
    main.mainloop()



mains()



