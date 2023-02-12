from collections import deque
from sys import stdin
m, n = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, stdin.readline().split())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([0, 0, -1, +1], [-1, +1, 0, 0]):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif array[nx][ny] == -1 or array[nx][ny] == 1:
                continue
            elif array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))
            else:
                if array[nx][ny] > array[x][y] + 1:
                    array[nx][ny] = array[x][y] + 1
                    queue.append((nx, ny))
                else:
                    continue 

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            bfs(i, j)

flag = 0
# if 0 이 하나라도 존재한다면 -1을 출력
# 구글링 해보자 간단한 식 있지 않을까?
for i in array:
    if 0 in i:
        flag = 1
        break

# 2차원 배열에서 max인 원소값을 찾기 -> 몰라서 구글링함
result = max(map(max, array))
if flag == 0:
    print(result - 1)
else:
    print(-1)


