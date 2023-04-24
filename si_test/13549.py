from collections import deque

visited = [False] * 100001

n, k = map(int, input().split())

def case(cur, c):
    if c == -1 or c == 1:
        return cur + c, 1
    else:
        return cur * 2, 0
    
def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        cur, time = queue.popleft()
        if cur == end:
            return time

        for c in [2, -1, 1]:
            new, ntime = case(cur, c)
            if not (0 <= new <= 100000):
                continue
            if visited[new]:
                continue
            queue.append((new, time + ntime))
            visited[new] = True
        

print(bfs(n, k))
