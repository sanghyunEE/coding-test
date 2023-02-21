n, k = map(int, input().split())

weight = [0]
value = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 물건 하나씩
    w = weight[i]
    v = value[i]
    for j in range(1, k + 1): # 1~k 무게까지 표 작성
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
print(dp[n][k])
for i in dp:
    print(i)
# https://www.youtube.com/watch?v=rhda6lR5kyQ&list=PLDV-cCQnUlIa0owhTLK-VT994Qh6XTy4v&index=11