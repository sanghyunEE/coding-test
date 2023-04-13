n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

if n == 1:
    print(10 % 10007)

else:
    for i, j in zip(range(9, 0, -1), range(1, 10)):
        dp[2][i] = j

    for i in range(3, n + 1):
        for j in range(9):
            dp[i][j + 1] = sum(dp[i - 1]) - sum(dp[i - 1][: j + 1])

    # for i in range(9):
    #     dp[3][i + 1] = sum(dp[2]) - sum(dp[2][: i + 1])

    # for i in range(9):
    #     dp[4][i + 1] = sum(dp[3]) - sum(dp[3][: i + 1])

    # for r in dp:
    #     print(r)

    # 2차원 배열 전체 합
    result = sum([sum(i) for i in dp])
    print(result % 10007)
