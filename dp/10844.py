n = int(input())

DP = [[0] * 10 for _ in range(100)]

for i in range(10):
    if i == 0:
        DP[0][i] = 0
    else:
        DP[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]

print(sum(DP[n-1]) % 1000000000)
# https://pacific-ocean.tistory.com/151