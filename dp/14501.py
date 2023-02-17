n = int(input())

t = []
p = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    t.append(x)
    p.append(y)

dp = [0] * 15
if n - t[0] >= 0:
    dp[0] = p[0]

for i in range(1, n):
    if n - i < t[i]:
        dp[i] = dp[i-1]
    else:
        for j in range(i): 
            if t[j] <= i - j: # j일에 시작해서 i일 전에 끝날 수 있을 때
                dp[i] = max(p[i] + dp[j], dp[i])
            else: # 못 끝낼때
                dp[i] = max(dp[i], dp[j], p[i])

print(max(dp))
print(dp)
# https://great-park.tistory.com/48