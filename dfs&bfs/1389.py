from collections import deque

def bfs(start):
    depth = [0] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        # print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                depth[i] += depth[v] + 1
    result[start] = sum(depth)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
result = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

# print(result)
print(result.index(min(result[1:])))