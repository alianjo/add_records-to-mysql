import tkinter
import mysql.connector
from tkinter import *
root = tkinter.Tk()
root.geometry('450x600')
root.title('create by Ali Anjo')

lab1 = tkinter.Label(root, text= 'Name',fg = 'blue',bg = 'yellow',font=('calibre',10,'bold')).grid(column=1, row=0)
 
lab2 = tkinter.Label(root, text= 'Family', fg = 'blue',bg = 'yellow',font=('calibre',10,'bold')).grid(column=1, row=2)
 
lab3 = tkinter.Label(root, text= 'International Number',bg = 'yellow', fg = 'blue',font=('calibre',10,'bold')).grid(column=1, row=3)
lab4 = tkinter.Label(root, text= 'Data base ',bg = 'yellow', fg = 'red',font=('calibre',10,'bold')).grid(column=1, row=4)
lab4 = tkinter.Label(root, text= 'Age ',bg = 'yellow', fg = 'blue',font=('calibre',10,'bold')).grid(column=1, row=5)
V_name= StringVar(root)
V_family= StringVar(root)
V_id= StringVar(root)
V_age = StringVar(root)
V_db= StringVar(root)

E1 = Entry(root, textvariable = V_name, bd=6).grid(column = 2, row=0)
E2 = Entry(root, textvariable = V_family, bd=6).grid(column = 2, row=2)
E3 = Entry(root, textvariable = V_id, bd=6).grid(column = 2, row=3)
E3 = Entry(root, textvariable = V_db, bd=6).grid(column = 2, row=4)
E3 = Entry(root, textvariable = V_age, bd=6).grid(column = 2, row=5)

def Add():
    try:
        co = mysql.connector.connect(host='localhost', user= 'ali', password='ila',database=V_db.get())
        cur = co.cursor()
        cur.execute("insert into users (name,last_name,id,age) values ('{}','{}','{}','{}');".format(V_name.get(),V_family.get(),int(V_id.get()),int(V_age.get())))
        co.commit()
        cur.close()
    except Exception as E:
        print('we hvae an error = ',E)
    else:
        global la
        la = Label(root,text='ok', fg='red').grid(column=3, row=8)
        
def show ():
    try:
        co = mysql.connector.connect(host='localhost', user= 'ali', password='ila',database=V_db.get())
        cur = co.cursor()
        res = cur.execute('select * from users;')
        global pl
        pl = {"column":2, "row":7}
        for i in cur.fetchall():
            global label1
            label1 = Label(root,text = str(i)).grid(**pl)
            pl["row"] +=1
        
        cur.close()
    except Exception as E:
        print('we have an Error :', E)
        
def res():
    V_name.set('')
    V_family.set('')
    V_id.set('')
    V_db.set('')
    V_age.set('')
    while pl['row']>=7:
        label1 = Label(root, text='                                                  ').grid(**pl)
        pl['row'] -=1 
    la = Label(root,text='  ', fg='red').grid(column=3, row=8)   
B1 = Button(root, text= 'Add', command=Add ,fg='blue').grid(column=3, row=6)
B2 = Button(root, text= 'Show', command=show ,fg='blue').grid(column=2, row=6)
B3 = Button(root, text= 'Reset', command=res ,fg='blue').grid(column=1, row=6)

root.mainloop()

