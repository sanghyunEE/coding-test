
x = int(input())
copy_x = x

group_num = 1
num = 0

i = 1
while x > 0:
    x = x - i
    if x <= 0:
        group_num = i
        num = i + x
        break
    i += 1

if group_num % 2 == 0:
    result = [1, group_num]
    for i in range(1, num):
        result[0] += 1
        result[1] -= 1 
else:
    result = [group_num, 1]
    for i in range(1, num):
        result[0] -= 1
        result[1] += 1


if copy_x == 1:
    print('1/1')
elif copy_x == 2:
    print('1/2')
elif copy_x == 3:
    print('2/1')
else:
    print(str(result[0]) + '/' + str(result[1]))



    