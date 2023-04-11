n = int(input())

dp = [0] * 21
dp[1] = 1


def go(x, start, middle, end):
    if x == 0:
        return
    go(x - 1, start, end, middle)
    print(start, end)
    go(x - 1, middle, start, end)
    
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 + dp[i - 1]
print(dp[n])
go(n, 1, 2, 3) # 1번에서 출발 2번은 n-1개의 종착지 3번은 최종목적