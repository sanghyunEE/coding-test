n, m = map(int, input().split())

data = list(map(int, input().split()))

result = 0
p = 0
end = 0

for start in  range(n):
    while p < m and end < n:
        p += data[end]
        end += 1
    if p == m:
        result += 1
    p -= data[start]

print(result)




