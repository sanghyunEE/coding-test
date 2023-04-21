
h, w, n, m = map(int, input().split())

wide = 0
while w > 0:
    wide += 1
    w -= (m + 1)

height = 0
while h > 0:
    height += 1
    h -= (n + 1)

result = wide * height
print(result)