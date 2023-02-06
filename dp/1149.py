n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

DP = [[0] * 3 for _ in range(n)]

DP[0][0] = data[0][0]
DP[0][1] = data[0][1]
DP[0][2] = data[0][2]

for i in range(1, n): # 1 ~ n-1 : data index
    for j in range(3): # 0 ~ 2 : rgb
        if j == 0:
            DP[i][j] = data[i][j] + min(DP[i-1][1], DP[i-1][2])
        elif j == 1:
            DP[i][j] = data[i][j] + min(DP[i-1][0], DP[i-1][2])
        else:
            DP[i][j] = data[i][j] + min(DP[i-1][0], DP[i-1][1])

print(min(DP[n-1]))