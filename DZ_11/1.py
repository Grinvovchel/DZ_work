from datetime import date

class MyDate:
    def __init__(self, string):
        self.date = string

    @classmethod
    def date_int(cls, obj):
        return obj.date.split('-')


    @staticmethod
    def valid():
        day=int(MyDate.date_int(a)[0])
        month=int(MyDate.date_int(a)[1])
        year=int(MyDate.date_int(a)[2])
        if 0 > day or day > 31:
            print ('Ввели неправельный день')

        if 0 > month or month > 12:
            print('Ввели неправельный месяц')

        if 2099 < year or year < 1970:
            print('Ввели неправельный год')



a = MyDate('12-8-2001')

print(MyDate.date_int(a))
print(type(MyDate.date_int(a)))
print(MyDate.valid())
a = MyDate('33-8-2022')
print(MyDate.date_int(a))
print(MyDate.valid())
a = MyDate('34-74-9999')
print(MyDate.date_int(a))
print(MyDate.valid())