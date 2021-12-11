i = 0
while i < 100:
    i += 1
    if i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif i % 10 >= 2 and i % 10 <= 4 and i != 12 and i != 13 and i != 14:
        print(i, 'процента')
    else:
        print(i, 'процентов')
