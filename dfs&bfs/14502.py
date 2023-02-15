from copy import deepcopy
from itertools import combinations

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

direction = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            direction.append((i, j))

real = list(combinations(direction, 3))

def dfs(arr, x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y] == 1 or arr[x][y] == 3:
        return False
    arr[x][y] = 3
    dfs(arr, x-1, y)
    dfs(arr, x+1, y)
    dfs(arr, x, y-1)
    dfs(arr, x, y+1)
    
    return True

result = []
for r in real:
    arr = deepcopy(array)
    for x in r:
        arr[x[0]][x[1]] = 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                dfs(arr, i, j)
    count = 0
    for i in arr:
        for j in i:
            if j == 0:
                count += 1
    result.append(count)

print(max(result))