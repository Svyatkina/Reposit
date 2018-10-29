import pprint
 
P=dict()
P['ПЕППЕРОНИ']={'Cостав':"Пепперони, моцарелла, томатный соус",'size':{'S':"395", 'M':"545"}}
P['МАРГАРИТА']={'Состав': 'Томаты, моцарелла, томатный соус','size':{'S':"395", 'M':"545"}}
P['ГАВАЙСКАЯ']={'Состав': 'Курица, ветчина, ананас, моцарелла, томатный соус','size':{'S':"415",'M':"595"}}
print('ДоДоПицца приветствует! \nПрограмма для заказа пиццы. \nСпасибо, что выбрали нашу компанию!')
print('Текущие заказы:')
with open('doc.txt','r') as file:
    content=file.readlines()
    print(content)

ad=input('Укажите адрес доставки: ')
date=input('Укажите дату(сегодня,завтра): ')
time= input('Укажите время: ')
c= input('Укажите контактные данные: ')
print('Пиццы в наличии:')
pprint.pprint(P)
D=dict()
l=[]
m=[]
i=1
while True:
    pizza=input('Укажите пиццу для заказа или "выход" для окончания ввода: ')
    
    if pizza.upper()=='ВЫХОД':
        print('Всего доброго! До свидания!')
        break
    elif pizza.upper() in P :
        choose_size=input('Укажите размер пиццы (S или M):')
        price=int(P[pizza.upper()]['size'][choose_size])
        k=int(input('Укажите количество: '))
        D[i]={'pizza': pizza.upper(),'count':k,'size':choose_size }
        l.append(k)
        m.append(price)
    else:
        continue
    i+=1
n=[]
for i in range(len(l)):
    Price=l[i]*m[i]
    n.append(Price)
fin_price=sum(n)

if sum(l)>=3:
    fin_price=fin_price - min(m)

if date.upper()=='ЗАВТРА':
    fin_price=fin_price-0.05*fin_price


print('Итог с учетом скидки:', fin_price)

D['adress']={ad}
D['contact']={c}
D['date']={date}
pprint.pprint(D)

print('Итог с учетом скидки:', fin_price)
print('Текущие заказы:')
with open('doc.txt','a') as output_file:
    output_file.writelines(str(D))

with open('doc.txt','r') as file:
    content=file.readlines()
    print(content)
print('Итог: ',fin_price , 'руб')
print('Заказ сформирован!')
