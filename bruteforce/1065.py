n = int(input())

result = 0
for i in range(1, n + 1):
    i = str(i)
    if len(i) == 1 or len(i) == 2:
        result += 1
    else:
        sub = int(i[0]) - int(i[1])
        flag = 0 # 등차가 아닐 때 : 1
        for j in range(2, len(i)):
            if int(i[j-1]) - int(i[j]) != sub:
                flag = 1
                break
        if flag == 0:
            result += 1
print(result)