import sys
sys.setrecursionlimit(10**6)
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    array = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        array[y][x] = 1 # 꺼꾸로 y x 해서 넣어야 함

    # 입력 : 시작 지점 좌표 / 출력 : Boolean
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if array[y][x] == 0:
            return False
        array[y][x] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    result = 0
    for x in range(m):
        for y in range(n):
            if dfs(x, y):
                result += 1

    print(result)

# https://computer-choco.tistory.com/462