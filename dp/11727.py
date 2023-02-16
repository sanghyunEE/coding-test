n = int(input())

DP = [0] * 1000
DP[0] = 1 # 1번째
DP[1] = 3
DP[2] = 5

for i in range(3, n):
    DP[i] = DP[i-1] + (DP[i-2] * 2)

print(DP[n-1] % 10007)

