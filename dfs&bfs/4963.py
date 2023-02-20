import sys
sys.setrecursionlimit(10**6)

dx = [+1, -1, 0, 0, +1, +1, -1, -1]
dy = [ 0, 0, +1, -1, -1, +1, -1, +1]

def dfs(x, y, h, w, arr):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if arr[x][y] == 0:
        return False
    arr[x][y] = 0
    for i, j in zip(dx, dy):
        dfs(x+i, y+j, h, w, arr)
    return True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, h, w, arr):
                result += 1
    print(result)