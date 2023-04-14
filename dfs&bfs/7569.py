import sys
from collections import deque

input = sys.stdin.readline
n, m, h = map(int, input().split())

array = []

for _ in range(h):
    temp = []
    for _ in range(m):
        temp.append(list(map(int, input().split())))
    array.append(temp)

# print()
# for h in array:    
#     for r in h:
#         print(r)
#     print()


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def check_zero(array):
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if array[i][j][k] == 0:
                    return True
    return False

def find_max(array):
    result = -1
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if array[i][j][k] > result:
                    result = array[i][j][k]
    return result

def bfs():
    # queue = deque()
    # queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()
        for i, j, k in zip(dx, dy, dz):
            nx, ny, nz = x + i, y + j, z + k
            if not (0 <= nx < m and 0 <= ny < n and 0 <= nz < h):
                continue
            if array[nz][nx][ny] in [-1, 1]:
                continue
            if array[nz][nx][ny] == 0:
                array[nz][nx][ny] = array[z][x][y] + 1
                queue.append((nx, ny, nz))
                continue
            if array[nz][nx][ny] > array[z][x][y] + 1:
                array[nz][nx][ny] = array[z][x][y] + 1
                queue.append((nx, ny, nz))

queue = deque()

if check_zero(array):
    for z in range(h):
        for x in range(m):
            for y in range(n):
                if array[z][x][y] == 1:
                    # bfs(x, y, z)
                    queue.append((x, y, z))
    bfs()
    if check_zero(array):
        print(-1)
    else:
        print(find_max(array) - 1)
else:
    print(0)



# print()
# for a in array:    
#     for r in a:
#         print(r)
#     print()
