import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if array[x][y] == 0:
        return False
    array[x][y] = 0
    global temp
    temp += 1
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x - 1, y)
    dfs(x + 1, y)
    return True

result = [0, 0]
temp = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result[0] += 1
            result[1] = max(result[1], temp)
            temp = 0

for i in result:
    print(i)