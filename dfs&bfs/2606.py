n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n + 1)


result = [0] # global 선언 할지 vs Argument로 넘길지
# 참고 : https://chanos.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-2606%EB%B2%88-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-DFS%EC%99%80-BFS-%EC%B0%A8%EC%9D%B4
# 또는 visited가 True인 것을 sum 하면 된다

def dfs(x):
    visited[x] = True
    result[0] += 1
    
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(result[0]-1)