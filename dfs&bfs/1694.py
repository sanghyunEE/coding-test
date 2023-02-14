# 얘는 -1 +1 이 있어서 DP로 못품 ㅇㅇ
# 부분 문제로 못 묶어 버림 

from collections import deque


MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs(n))
