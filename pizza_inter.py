P=dict() 
P['ПЕППЕРОНИ']={'Cостав':"Пепперони, моцарелла, томатный соус",'size':{'S':"395", 'M':"545"}} 
P['МАРГАРИТА']={'Состав': 'Томаты, моцарелла, томатный соус','size':{'S':"395", 'M':"545"}} 
P['ГАВАЙСКАЯ']={'Состав': 'Курица, ветчина, ананас, моцарелла, томатный соус','size':{'S':"415",'M':"595"}} 
import tkinter 
import tkinter.ttk 

root = tkinter.Tk() 


tkinter.Label(root, text='Выберите пиццы:', borderwidth=8).grid(row=0,column=0) 
tkinter.Label(root, text='Выберите размер:', borderwidth=8).grid(row=0,column=1) 
tkinter.Label(root, text='Укажите количество:', borderwidth=8).grid(row=0,column=2) 


for i in range (len(list(P))):
    tkinter.Label(root, text=list(P)[i], borderwidth=8).grid(row=i+1,column=0)
    

a=tkinter.StringVar()
tkinter.ttk.Combobox(root, values=list (P['ПЕППЕРОНИ']['size'].keys()),textvariable=a).grid(row=1,column=1)
a1=a.get()

b=tkinter.StringVar()
tkinter.ttk.Combobox(root, values=list (P['МАРГАРИТА']['size'].keys()),textvariable=b).grid(row=2,column=1)
b1=b.get()
c=tkinter.StringVar()
tkinter.ttk.Combobox(root, values=list (P['ГАВАЙСКАЯ']['size'].keys()),textvariable=c).grid(row=3,column=1)
c1=c.get()

 
d=tkinter.StringVar()
tkinter.Spinbox(root, from_=0, to_=20,textvariable=d).grid(row=1,column=2)

g=tkinter.StringVar()
tkinter.Spinbox(root, from_=0, to_=20,textvariable=g).grid(row=2,column=2)

h=tkinter.StringVar()
tkinter.Spinbox(root, from_=0, to_=20,textvariable=h).grid(row=3,column=2)




tkinter.Label(root, text='Введите время заказа:', borderwidth=8).grid(row=5,column=0) 
tkinter.Label(root, text='Введите ваш адрес:', borderwidth=8).grid(row=5,column=1) 
tkinter.Label(root, text='Введите номер телефона:', borderwidth=8).grid(row=5,column=2) 

 
L=[]
for i in range(3):
    e=tkinter.StringVar()
    tkinter.Entry(root, borderwidth=8,textvariable=e).grid(row=6,column=i)
    L.append(e)

tkinter.Label(root, text='Выберите дату заказа:', borderwidth=8).grid(row=7,column=1) 
f=tkinter.StringVar()     
tkinter.ttk.Combobox(root, values=['сегодня','завтра'],textvariable=f).grid(row=8,column=1)


def price():
    
    p=(int(d.get())*int(P['ПЕППЕРОНИ']['size'][a.get()]))+(int(g.get())*int(P['МАРГАРИТА']['size'][b.get()]))+(int(h.get())*int(P['ГАВАЙСКАЯ']['size'][c.get()]))
    if sum([int(d.get()),int(g.get()),int(h.get())])>=3:
        p=p-min([int(P['ПЕППЕРОНИ']['size'][a.get()]),int(P['МАРГАРИТА']['size'][b.get()]),int(P['ГАВАЙСКАЯ']['size'][c.get()])])
    else:
        p=p
    if f.get()=='завтра':
        p=p-0.05*p
    else:
        return p
    price1.set(p)
    
    




price1=tkinter.IntVar()
tkinter.Label(root, text='Cумма заказа с учетом скидки:', borderwidth=8).grid(row=9,column=1) 
label = tkinter.Label(root,textvariable=price1).grid(row=10,column=1)
button = tkinter.Button(root,text='Заказать', command=price).grid(row=11,column=1)



    

