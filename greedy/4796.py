num = 0
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    total = 0
    result = 0
    diff = p - l
    flag = 0 # 0 : l / 1 : diff
    while True:
        if flag == 0:
            if total + l > v:
                result = result + (v - total)
                break
            else:
                result = result + l
                total = total + l
            flag = 1
        else:
            if total + diff > v:
                break
            else:
                total = total + diff
            flag = 0

    num += 1
    print('Case ' + str(num) + ':', result)