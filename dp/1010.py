
dp = [0] * 31
dp[0] = 1 # 0!
dp[1] = 1 # 1!
dp[2] = 2 # 2!

for i in range(3, 31):
    dp[i] = dp[i-1] * i

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    up = m
    left = m - n
    right = n

    result = dp[m] / (dp[left] * dp[right])

    print(round(result))