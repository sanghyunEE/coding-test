
n, k = map(int, input().split())

dp = [0] * 10001

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()

def find_min(i):
    ret = 10001
    for coin in coins:
        if coin == i:
            ret = 1
        if i > coin:
            if dp[i - coin] == 0: continue
            ret = min(ret, dp[i - coin] + 1)
        else:
            continue
    if ret == 10001: return 0
    # print(ret)
    return ret

for i in range(1, k + 1):
    dp[i] = find_min(i)

# print(dp[:16])

if dp[k] == 0: print(-1)
else: print(dp[k])