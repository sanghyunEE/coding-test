from collections import deque
from math import floor

n = int(input())
board = [] # 현재 상황판

sx, sy = 0, 0 # 아기상어 시작점
shark = 2 # 아기상어 크기
for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        sx, sy = i, temp.index(9)
    board.append(temp)

result = 0 # 진행 시간 (초)

# 먹을 물고기들의 위치 리스트 반환
def is_eatable():
    ret = []
    for i in range(n):
        for j in range(n):
            if floor(shark) > board[i][j] and board[i][j] > 0 and board[i][j] != 9:
                ret.append((i, j))
    return ret

# 현재 상어 위치에서 모든 곳으로 가기 까지의 패스 길이
def eat():
    temp = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((sx, sy))
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if sx == nx and sy == ny:
                continue
            if (0 <= nx < n and 0 <= ny < n) and temp[nx][ny] == 0:
                if board[nx][ny] > shark:
                    continue
                temp[nx][ny] = temp[x][y] + 1
                queue.append((nx, ny))
    return temp

# for i in eat():
#     print(i)

fish_list = is_eatable()
# print(fish_list)
while fish_list:
    if len(fish_list) == 1:
        path = eat()
        x, y = fish_list[0] # target 물고기의 위치
        # print('eat :', (x, y), path[x][y])
        if path[x][y] != 0:
            board[sx][sy] = 0 # 현재 샤크의 보드 0으로 초기화
            sx, sy = x, y # sx sy 의 위치 변수 업데이트
            shark += (1 / floor(shark)) # 샤크의 크기 
            result += path[x][y] # 진행 시간 업데이트
            board[x][y] = 9 # 현재 샤크의 보드판 표시 업데이트
        else:
            break
        
    else:
        path = eat()
        target = []
        # for p in path:
            # print(p)
        # fish_list.sort(key=lambda x: (x[0], x[1]))
        for x, y in fish_list:
            # print(x,y)
            if not target and path[x][y] != 0:
                target.append((x, y))
                continue
            if target:
                px, py = target[0]
                if path[px][py] > path[x][y] and path[x][y] != 0:
                    target.clear()
                    target.append((x, y))
                elif path[px][py] == path[x][y]:
                    target.append((x, y))

        target.sort(key=lambda x: (x[0], x[1]))
        if not target:
            break

        x, y = target[0]
        # print(fish_list)
        # print(target)
        # print('eat :', (x, y), path[x][y])
        if path[x][y] != 0:
            board[sx][sy] = 0
            sx, sy = x, y
            shark += (1 / floor(shark))
            result += path[x][y]
            board[x][y] = 9
        else:
            break
    fish_list = is_eatable()
    # print(fish_list)
    # for b in board:
        # print(b)
    # print(result, floor(shark), shark)
    # print()

print(result)

# 찾았다 내사랑
# https://www.acmicpc.net/board/view/93917
# https://www.acmicpc.net/board/view/100027