n = int(input())

data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

data.sort(key = lambda x : (x[1], x [0]))

result = 1
current = data[0][1]
for i in range(1, n):
    if data[i][0] >= current:
        result += 1
        current = data[i][1]
print(result)

# (x, y) 일 때 y 를 기준으로 정렬 후 x 를 기준으로 정렬하는 것이 키포인트