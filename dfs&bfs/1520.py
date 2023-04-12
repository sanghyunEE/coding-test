import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

m, n = map(int, input().split())

array = []
for _ in range(m):
    array.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def go(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and array[x][y] > array[nx][ny]:
            ways += go(nx, ny)

    dp[x][y] = ways
    return ways




print(go(0, 0))

