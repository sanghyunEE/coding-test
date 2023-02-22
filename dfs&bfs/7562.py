from collections import deque
t = int(input())
for _ in range(t):
    size = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    array = [[0] * size for _ in range(size)]
    array[sx][sy] = 1

    dx = [-2, -2, -1, -1, +1, +1, +2, +2]
    dy = [-1, +1, -2, +2, -2, +2, -1, +1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i, j in zip(dx, dy):
                nx = x + i
                ny = y + j
                if nx < 0 or nx >= size or ny < 0 or ny >= size:
                    continue
                if array[nx][ny] != 0:
                    continue
                if nx == ex and ny == ey:
                    array[nx][ny] = array[x][y] + 1
                    return(array[nx][ny])
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))

    if sx == ex and sy == ey:
        print(0)
    else:
        print(bfs(sx, sy) - 1)
