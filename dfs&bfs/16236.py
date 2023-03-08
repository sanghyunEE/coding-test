from collections import deque
n = int(input())

fish = 0 # 남아있는 물고기 마릿수
sx, sy = 0, 0 # 아기상어의 현재 위치 
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    for c, i in zip(row, range(n)):
        if c in [1, 2, 3, 4, 5, 6]:
            fish += 1
        elif c == 9:
            sx = _
            sy = i
    array.append(row)

result_time = 0 # 답

dx = [0, 0, +1, -1]
dy = [-1, +1, 0, 0]

def go():
    if fish == 0:
        return 0
    
    size = 2 # 상어 현재 사이즈
    st = 0 # 축적분

    array[sx, sy] = -1 # 초기 변환
    queue = deque()
    queue.append((sx, sy))

    while fish > 0:
        times = [[0] * n for i in range(n)]
        while queue:
            sx, sy = queue.popleft()
            for i, j in zip(dx, dy):
                nx = sx + i
                ny = sx + j

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue    
                if array[nx][ny] == 0:
                    continue
                if array[nx][ny] > size or array[nx][ny] == size:
                    continue
                

        



print(go())

