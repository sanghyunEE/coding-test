n = int(input())

score = []
for _ in range(n):
    score.append(int(input()))

DP = [0] * n
DP[0] = score[0]

if n == 2:
    DP[1] = score[0] + score[1]

elif n >= 3:
    DP[1] = score[0] + score[1]
    DP[2] = max(score[1] + score[2], score[0] + score[2])
    for i in range(3, n):
        DP[i] = max(DP[i-3] + score[i-1] + score[i] , DP[i-2] + score[i])

print(DP[n-1])

# https://daimhada.tistory.com/181