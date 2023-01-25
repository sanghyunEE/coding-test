t = int(input())

for i in range(t):
    n = int(input())

    DP_0 = [0] * 41
    DP_1 = [0] * 41

    DP_0[0] = 1
    DP_1[0] = 0

    DP_0[1] = 0
    DP_1[1] = 1

    for i in range(2, n + 1):
        DP_0[i] = DP_0[i-1] + DP_0[i-2]
        DP_1[i] = DP_1[i-1] + DP_1[i-2]

    print(DP_0[n], DP_1[n])
