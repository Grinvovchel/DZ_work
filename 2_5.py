import math

my_list = [5.68, 24.07, 0.8, 34.25, 67, 55, 87.07, 42.67, 55.5]
print(id(my_list))
print('___________________________')
my_list.sort()
for i in my_list:
    a = i * 100
    rub = math.floor(a // 100)
    cop = math.floor(a % 100)
    # print(rub,'руб',cop,'коп')
    if rub < 10:
        rub = '0' + str(rub)
    if cop < 10:
        cop = '0' + str(cop)
    print(rub, 'руб', cop, 'коп')
print('___________________________')
print(id(my_list))
print('___________________________')
my_list2 = my_list
my_list2.sort(reverse=True)
for i in my_list2:
    a = i * 100
    rub = math.floor(a // 100)
    cop = math.floor(a % 100)
    # print(rub,'руб',cop,'коп')
    if rub < 10:
        rub = '0' + str(rub)
    if cop < 10:
        cop = '0' + str(cop)
    print(rub, 'руб', cop, 'коп')
print('___________________________')
max_5 = sorted(my_list, reverse=True)[:5]
for i in max_5:
    a = i * 100
    rub = math.floor(a // 100)
    cop = math.floor(a % 100)
    # print(rub,'руб',cop,'коп')
    if rub < 10:
        rub = '0' + str(rub)
    if cop < 10:
        cop = '0' + str(cop)
    print(rub, 'руб', cop, 'коп')
