import sys
input = sys.stdin.readline
from copy import deepcopy
sys.setrecursionlimit(10 ** 4)

# 깊은 복사는 deep copy 대신 slicing 활용
# https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B9%8A%EC%9D%80%EB%B3%B5%EC%82%AC%EB%8A%94-deepcopy%EA%B0%80-%EB%B9%A0%EB%A5%BC%EA%B9%8C-slicing%EC%9D%B4-%EB%B9%A0%EB%A5%BC%EA%B9%8C

n, m = map(int, input().split())

curr_ice = []
for _ in range(n):
    curr_ice.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def next_ice(curr_ice):
    temp = [i[:] for i in curr_ice]
    for i in range(n): # 300
        for j in range(m): # 300
            if curr_ice[i][j] == 0:
                continue
            else:
                for x, y in zip(dx, dy):
                    if curr_ice[i + x][j + y] == 0:
                        if temp[i][j] - 1 < 0: continue
                        else: temp[i][j] = temp[i][j] - 1
    return temp

# curr_ice = next_ice(curr_ice)
# for _ in curr_ice:
#     print(_)

def dfs(x, y, visited):
    visited[x][y] = True
    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        # print(nx, ny)
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if curr_ice[nx][ny] == 0:
            continue
        else:
            # print(visited[nx][ny], nx, ny)
            if not visited[nx][ny]:
                # print(nx, ny)
                dfs(nx, ny, visited)
    return True

# a = [[False] * m for _ in range(n)]
# result = 0
# for i in range(n):
#     for j in range(m):
#         if curr_ice[i][j] == 0:
#             continue
#         elif not a[i][j] and dfs(i, j, a):
#             result += 1
#         for f in a:
#             print(f)
#         print()
# # for i in a:
# #     print(i)
# print(result)

def is_all_zero():
    flag = True
    for i in range(n):
        for j in range(m):
            if curr_ice[i][j] != 0:
                flag = False
                break
        if flag:
            break
    if not flag: return True
    else: return False
# print(is_all_zero())

year = 0 # 현재 진행 년수
while True:
    curr_ice = next_ice(curr_ice)
    for _ in curr_ice:
        print(_)
    year += 1 # 년수 추가
    partition = 0 # 덩어리 개수
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if partition >= 2:
                break
            if curr_ice[i][j] == 0:
                continue
            else:
                if not visited[i][j] and dfs(i, j, visited):
                    print('실행', i, j, year)
                    partition += 1

    # print(partition)
    if partition >= 2:
        break
    if is_all_zero():
        year = 0
        break
print(year)

    
