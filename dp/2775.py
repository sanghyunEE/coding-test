t = int(input())

for i in range(t):
    # k층, n호
    k = int(input())
    n = int(input())

    # 14층(0~14 : 15개) 14호
    DP = [[0] * 14 for _ in range(15)]

    for i in range(len(DP[0])):
        DP[0][i] = i + 1

    # i: 층 / j: 호
    for i in range(1, k + 1): # 1 ~ 14
        for j in range(0, n): # 0 ~ 13
            DP[i][j] = sum(DP[i-1][0:j+1])

    print(DP[k][n-1])