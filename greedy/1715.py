import sys
input = sys.stdin.readline

cards = []
result = 0

n = int(input())

for _ in range(n):
    cards.append(int(input()))
cards.sort()

result = 0
if n == 1:
    print(0)
else:
    while len(cards) >= 2:
        a, b = cards.pop(0), cards.pop(0)
        result += a + b
        cards.append(a + b)
        cards.sort()
print(result)
