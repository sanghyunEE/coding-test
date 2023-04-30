n = int(input())

data = list(map(int, input().split()))

result = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == data[i] and result[j] == 0:
            result[j] = i + 1
            cnt = 0
            break
        if result[j] == 0:
            cnt += 1
    # print(result)


print(' '.join(map(str, result)))