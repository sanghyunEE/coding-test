from sys import setrecursionlimit
from copy import deepcopy
setrecursionlimit(10**6)

n = int(input())

array = []
for _ in range(n):
    array.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_r(arr, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1 or arr[x][y] == 'G' or arr[x][y] == 'B':
        return False
    arr[x][y] = 1
    for i, j in zip(dx, dy):
        dfs_r(arr, x+i, y+j)
    return True
def dfs_g(arr, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1 or arr[x][y] == 'R' or arr[x][y] == 'B':
        return False
    arr[x][y] = 1
    for i, j in zip(dx, dy):
        dfs_g(arr, x+i, y+j)
    return True
def dfs_b(arr, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1 or arr[x][y] == 'R' or arr[x][y] == 'G':
        return False
    arr[x][y] = 1
    for i, j in zip(dx, dy):
        dfs_b(arr, x+i, y+j)
    return True
def dfs_rg(arr, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1 or arr[x][y] == 'B':
        return False
    arr[x][y] = 1
    for i, j in zip(dx, dy):
        dfs_rg(arr, x+i, y+j)
    return True

array_rg = deepcopy(array)
count = 0
count_rg = 0
for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            if dfs_r(array, i, j):
                count += 1
        elif array[i][j] == 'G':
            if dfs_g(array, i, j):
                count += 1
        else:
            if dfs_b(array, i, j):
                count += 1
print(count)

for i in range(n):
    for j in range(n):
        if array_rg[i][j] == 'R' or array_rg[i][j] == 'G':
            if dfs_rg(array_rg, i, j):
                count_rg += 1
        else:
            if dfs_b(array_rg, i, j):
                count_rg += 1
print(count_rg)