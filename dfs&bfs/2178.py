from collections import deque

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        v = queue.popleft()
        for i, j in zip(dx, dy):
            nx = v[0] + i
            ny = v[1] + j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if not visited[nx][ny]:
                queue.append((nx, ny))
                array[nx][ny] += array[v[0]][v[1]]
                visited[nx][ny] = True

bfs(0, 0)
print(array[n-1][m-1])
