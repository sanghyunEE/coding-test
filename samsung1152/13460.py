from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

rx, ry, bx, by, hx, hy = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'O':
            hx, hy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by = queue.popleft()

        for i in range(4):
            
