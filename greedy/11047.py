# n: 동전의 종류 개수 / k: 목표 금액
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()

result = 0
for coin in coins:
    if k // coin >= 1:
        result += k // coin
        k %= coin

print(result)
