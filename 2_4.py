my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in my_list:
    # print(i.title())
    # print(i.rsplit(' ',1)[-1])
    print('Привет,', i.rsplit(' ', 1)[-1].title(), '!', sep='', end=' ')
