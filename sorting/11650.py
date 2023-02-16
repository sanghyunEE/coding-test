# heap sort로 풀어야 하는지
n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[0], x[1]))

for i in data:
    print(i[0], i[1])