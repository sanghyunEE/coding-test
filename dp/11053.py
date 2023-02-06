# Hint : DP[i] = array[i] 를 마지막 원소로 가지는 부분수열의 최대 길이

n = int(input())

array = list(map(int, input().split()))

DP = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            DP[i] = max(DP[j] + 1, DP[i])
print(max(DP))