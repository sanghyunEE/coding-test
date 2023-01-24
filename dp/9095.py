t = int(input())

DP = [0] * 11
DP[0] = 1
DP[1] = 2
DP[2] = 4

for _ in range(t):
    n = int(input())
    for i in range(3, n):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    print(DP[n-1])

# 참고
# https://myjamong.tistory.com/302