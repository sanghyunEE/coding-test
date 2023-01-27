n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


flags = [[0] * n for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0
    flags[x][y] = flag
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

result = 0
flag = 1
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result += 1
            flag += 1

print(result)
list = []
for i in range(1, flag):
    count = 0
    for array in flags:
        for j in array:
            if i == j:
                count += 1
    list.append(count)
list.sort()
for i in list:
    print(i)
