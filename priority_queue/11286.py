import heapq, sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x)) # 튜플 heap 정렬 유의
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)

# 처음 푼 것 처럼 max heap + min heap 으로 해도 된다.



