my_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(my_list)):
   if my_list[i]=='5':
        my_list[i]='05'
   elif my_list[i]=="+5":
       my_list[i]='+05'
# print(my_list)
my_list.insert(1,'"')
my_list.insert(3,'"')
my_list.insert(5,'"')
my_list.insert(7,'"')
my_list.insert(12,'"')
my_list.insert(14,'"')
# print(' '.join(my_list))
print((my_list.rsplit(' ',sep='"'))

