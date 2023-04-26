import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = list(map(int, input().split()))

prefix_sum = [0]
for i in range(1, n + 1):
    prefix_sum.append(data[i - 1] + prefix_sum[i - 1])
# print(prefix_sum)

result = []
for i in range(0, n + 1 - k):
    result.append(prefix_sum[i + k] - prefix_sum[i])

# print(result)
print(max(result))