k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines) # 왜 max 로 둬야하지??

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in lines:
        if i // mid > 0:
            total += i // mid
    
    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# https://only-wanna.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1654%EB%B2%88-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0