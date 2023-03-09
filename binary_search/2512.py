n = int(input())
data = list(map(int, input().split()))
m = int(input())

start = 1
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for i in data:
        if mid >= i:
            sum_budget += i
        else:
            sum_budget += mid

    if sum_budget <= m:
        start = mid + 1
        result = start
    else:
        end = mid - 1

print(result - 1)