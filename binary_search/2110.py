import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 입력이 많으니 sys로 받아라
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # nlogn 20만 가능

start, end = 1, array[-1] - array[0]

result = 0

if c == 2:
    print(array[-1] - array[0])
else:
    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        last = array[0]
        for i in range(1, n):
            if array[i] - last >= mid:
                cnt += 1
                last = array[i]
        if cnt >= c: # 이 부분이 헷갈림
            result = mid
            start = mid + 1
        else: 
            end = mid -1
    print(result) # print를 else문 밖에다 넣으면 안되지 상현아..

# https://hongcoding.tistory.com/3
# https://my-coding-notes.tistory.com/119
# 이분탐색 파라메트릭서치 좀더 공부