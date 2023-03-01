import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
# m : 행개수 / n : 열개수 / k : 색칠한 직사각형 개수

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())

    # 좌측 아래 좌표
    row = m - 1 - ly
    col = lx
    squares = [] # 색칠할 애들 좌표 리스트
    for i in range(ry - ly):
        for j in range(rx - lx):
            squares.append((row - i, col + j))
    for r, c in squares:
        graph[r][c] = 1

region = 0
def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        return False
    global region
    graph[x][y] = 1
    region += 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


array = []
result = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            result += 1
            array.append(region)
            region = 0

print(result)
for i in sorted(array):
    print(i, end=' ')
