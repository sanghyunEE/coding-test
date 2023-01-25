n = int(input())

DP = [0] * (n + 1)
DP[0] = 0
DP[1] = 0

for i in range(2, n + 1):
    result = 1e6 + 1
    if i % 3 == 0:
        result = min(result, DP[i//3])
    if i % 2 == 0:
        result = min(result, DP[i//2])
    result = min(result, DP[i-1])
    DP[i] = result + 1
        
print(DP[n])
