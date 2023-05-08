# 1. 해쉬 dict로 풀기
# 2. 투포인터로 풀기

n = int(input())
m = int(input())

data = list(map(int, input().split()))
data.sort()

start = 0
end = len(data) - 1
result = 0
while start != end:
    if data[start] + data[end] == m:
        result += 1
        start += 1
    elif data[start] + data[end] < m:
        start += 1
    else:
        end -= 1
print(result)