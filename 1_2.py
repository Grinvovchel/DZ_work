my_list = []
for i in range(1, 1000, 2):
    my_list.append(i ** 3)
print((my_list))
my_list2 = []
sum1 = 0
for num in my_list:
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        my_list2.append(i)
    sum1 = 0
print(sum(my_list2))
sum_num_plus = 0
for num in my_list:
    summ = 0
    i = num
    num += 17
    while num != 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        sum_num_plus += i
print(sum_num_plus)
