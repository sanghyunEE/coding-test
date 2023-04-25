import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

# 거리 1 마다 노드로 판단해서 dist 1로 초기화 해주기
for i in range(d):
    graph[i].append((i + 1, 1))

# 지름길 graph 추가
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d: # 역주행 할 수 없으므로 무시해도 됨
        continue
    else: graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])



