from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    # 혹시 append 하면서 정렬하면서 넣는건 없나..

# 오름차순 정렬 -> N이 100으로 맥스고 NlogN 이 되니까 상관없지??ㅇㅇ 
for i in graph:
    i.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')

    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)

# visited 를 True로 해야하는 시점이 헷갈렸다.
def bfs(x):
    queue = deque()
    queue.append(x)
    visited_bfs[x] = True

    while queue:
        n = queue.popleft() # 꺼낸 노드
        print(n, end=' ')
        
        for i in graph[n]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


dfs(v)
print()
bfs(v)

