from sys import stdin, setrecursionlimit
from copy import deepcopy
setrecursionlimit(10**6)

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, stdin.readline().split())))

def dfs(arr, x, y, t):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] <= t or arr[x][y] == 0:
        return False
    arr[x][y] = 0
    dfs(arr, x-1, y, t)
    dfs(arr, x+1, y, t)
    dfs(arr, x, y-1, t)
    dfs(arr, x, y+1, t)
    return True

# min_val = min(map(min, array)) # 비가 안오는 경우도 구해야한다..
min_val = 0
max_val = max(map(max, array))

current = -1
for t in range(min_val, max_val + 1):
    region = 0
    arr = deepcopy(array) # deep copy 써라
    for i in range(n):
        for j in range(n):
            if dfs(arr, i, j, t):
                region += 1
    current = max(current, region)

print(current)