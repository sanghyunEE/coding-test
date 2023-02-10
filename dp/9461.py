t = int(input())

DP = [0] * 100
DP[0], DP[1], DP[2], DP[3], DP[4] = 1, 1, 1, 2, 2

for _ in range(t):
    n = int(input())

    for i in range(5, n):
        DP[i] = DP[i-1] + DP[i-5]
    
    print(DP[n-1])

# 왜 런타임 에러?
# DP 배열을 [0] * n 으로 했더니 런타임 에러 났음 ㅇㅇ

