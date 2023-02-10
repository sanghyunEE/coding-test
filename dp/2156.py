# 이코테 개미전사랑 비슷한듯 + 계단 올라가기 DP 문제랑 비슷

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

DP = [0] * 10000 # [0] * n 보다 10000 같은 상수 넣어주는게 런타임 에러 줄여 줌

if n == 1:
    print(array[0])
elif n == 2:
    print(array[0] + array[1])
else:
    DP[0] = array[0]
    DP[1] = array[0] + array[1]
    DP[2] = max(array[0] + array[1], array[0] + array[2], array[1] + array[2])

    for i in range(3, n):
        # DP[i-1] 안써서 처음에 틀림... ㅠㅠ 경우의 수 세가지임을 이해하는게 중요
        DP[i] = max(array[i] + array[i-1] + DP[i-3], array[i] + DP[i-2], DP[i-1])
    print(max(DP)) 
