pay = int(input())

value = 1000 - pay

result = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    if value // coin >= 1:
        result += value // coin
        value = value % coin

print(result)
