# 아이디어 : DP
# 시간복잡도 : O(N)
# 변수 : DP 

n = int(input())
array = list(map(int, input().split()))

DP = [0] * n
DP[0] = array[0]

for i in range(1, n):
    DP[i] = max(array[i], DP[i-1] + array[i])
print(max(DP))