n = int(input())

data = []
for idx in range(n):
    x, y = map(int, input().split())
    data.append([x, y, idx, 1])
data.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    for j in range(i + 1, n):
        if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            data[i][3] += 1

for i in sorted(data, key= lambda x: x[2]):
    print(i[3], end=' ')