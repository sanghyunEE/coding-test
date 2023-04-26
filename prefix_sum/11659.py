import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

for _ in range(m):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left - 1])
