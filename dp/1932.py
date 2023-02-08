# dp는 최대 합의 결과를 찾으라하지 경로를 찾으라 하지 않는다 대개
# 물론 경로를 찾을 순 있다. 대신 메모리 엄청 많이 되서 시간초과 나지
# f(i) 는 f(i-n)의 영향을 받음을 항상 기억

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

DP = [[0] * x for x in range(1, n + 1)] # initialize 주의
DP[0][0] = data[0][0]

for i in range(1, n): # 1부터 시작 range(0) 하면 idx 오류
    for j in range(len(data[i])):
        if j == 0:
            DP[i][j] = DP[i-1][0] + data[i][j]
        elif j == i:
            idx = len(data[i-1]) - 1
            DP[i][j] = DP[i-1][idx] + data[i][j]
        else:
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + data[i][j]

print(max(DP[n-1]))

