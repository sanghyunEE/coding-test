import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

result, prefix_sum, end = 100001, 0, 0

# while start < n and end < n:
#     prefix_sum = sum(data[start:end + 1])
#     print(prefix_sum)
#     if prefix_sum == s:
#         result = min(result, end - start + 1)
#         end += 1
#     elif prefix_sum > s: start += 1
#     else: end += 1

for start in range(n):
    while prefix_sum < s and end < n:
        prefix_sum += data[end]
        end += 1
    if prefix_sum >= s:
        result = min(result, end - start)
    prefix_sum -= data[start]    

if result == 100001: print(0)
else: print(result)

