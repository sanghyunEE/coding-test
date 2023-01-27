n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n + 1)


result = [0] # global 선언 할지 vs Argument로 넘길지

def dfs(x):
    visited[x] = True
    result[0] += 1
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(result[0]-1)