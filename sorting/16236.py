import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
data.sort(key = lambda x: (x[1], x[0]))

for i in data:
    print(i[0], i[1])