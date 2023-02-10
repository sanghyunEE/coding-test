# 이코테 dfs 문제랑 비슷
from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)] # [[] * (n + 1)] 주의!!!!!

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

# # 각 노드별로 오름차순 할 필요가 있나?? 있는듯??
# for i in range(1, n + 1):
#     graph[i].sort()

visited = [False] * (n + 1)

# dfs 공식이 아직도 부족한거같다.. 외워라 이해하고..
def dfs(x):
    if not visited[x]:
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                dfs(i)
        return True
    else:
        return False

result = 0
for x in range(1, n + 1):
    if dfs(x):
        result += 1

print(result)

# RecursionError 발생함..
# https://dmaolon00.tistory.com/72
# sys.setrecursionlimit(10000) 