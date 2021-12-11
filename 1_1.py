duration = int(input("введите число"))
day = duration // 86400
day_remains = duration - day * 86400
hour = day_remains // 3600
hour_remains = day_remains - hour * 3600
minutes = hour_remains // 60
second = hour_remains - minutes * 60
if duration > 86400:
    print(day, 'дней', hour, 'часов', minutes, 'минут', second, 'секунд')

elif duration > 3600:
    print(hour, 'часов', minutes, 'минут', second, 'секунд')

elif duration > 60:
    print(minutes, 'минут', second, 'секунд')

else:
    print(second, 'секунд')
