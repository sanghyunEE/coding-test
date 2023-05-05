import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    x = int(input())
    graph[x].append(i)

# print(graph)


def dfs(v, p):
    # print(v, p)
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, p)
        elif visited[i] and i == p:
            # print(v, p, '에서')
            # 싸이클인 노드이구나
            result.append(i)

result = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)
    # print()

print(len(result))
for i in sorted(result):
    print(i)
