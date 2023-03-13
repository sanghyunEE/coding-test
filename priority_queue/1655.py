import heapq
import sys
input = sys.stdin.readline

n = int(input())

left_heap = []
right_heap = []
mid_value = 10001

for _ in range(n):
    x = int(input())
    if mid_value == 10001:
        mid_value = x
        print(mid_value)
        continue
    
    if x >= mid_value:
        heapq.heappush(right_heap, x)
    else:
        heapq.heappush(left_heap, -x)
    
    if abs(len(left_heap) - len(right_heap)) >= 2:
        if len(left_heap) > len(right_heap):
            l = -heapq.heappop(left_heap)
            heapq.heappush(right_heap, mid_value)
            mid_value = l
        else:
            r = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -mid_value)
            mid_value = r
    print(mid_value, '@@@')