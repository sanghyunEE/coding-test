# 열 n
n = int(input())

DP = [0] * 1000 # 0~999 idx
DP[0] = 1
DP[1] = 2

for i in range(2, n):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[n-1] % 10007)

# pypy3 로 했더니 런타임에러 안남
# python3 로 하면 런타임 에러 남
# https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726-2xn-%ED%83%80%EC%9D%BC%EB%A7%81-%ED%95%B4%EC%84%A4-python