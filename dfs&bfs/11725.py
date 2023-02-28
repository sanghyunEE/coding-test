import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, n + 1):
    graph[i].sort()
# print(graph)

parent_node = [0] * (n + 1)
visited = [False] * (n + 1)
def dfs(x, prev): # x : start
    visited[x] = True
    parent_node[x] = prev
    for i in graph[x]:
        if not visited[i]:
            dfs(i, x)
    
dfs(1, 0)
for i in range(2, n + 1):
    print(parent_node[i])

