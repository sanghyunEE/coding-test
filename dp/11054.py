

n = int(input())

data = list(map(int, input().split()))
revs_data = list(reversed(data))

increase = [1] * n
decrease = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(1, n):
    for j in range(i):
        if revs_data[i] > revs_data[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

decrease.reverse()
print(increase)
print(decrease)

dp = [0] * n

for i in range(n):
    dp[i] = increase[i] + decrease[i] - 1

print(max(dp))

# result = 0
# for i in range(n - 1):
#     a, b = increase[:i + 1], decrease[i + 1:]
#     print(a, b)
#     slice_sum = max(increase[:i + 1]) + max(decrease[i + 1:])
#     result = max(result, slice_sum)

# print(result)