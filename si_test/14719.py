h, w = map(int, input().split())

data = list(map(int, input().split()))

result = 0
# height 만큼 반복
for _ in range(h):
    # print(data)
    flag = False
    temp = 0
    for i in range(w):
        if data[i] > 0 and flag == True:
            result += temp
            temp = 0
            continue
        if i == w and data[i] == 0:
            temp = 0
            break
        if flag == True and data[i] == 0:
            temp += 1
        if data[i] > 0:
            result += temp
            flag = not flag
            temp = 0
    for i in range(w):
        if data[i] > 0:
            data[i] -= 1
    # print(result)
    # result += temp

print(result)
