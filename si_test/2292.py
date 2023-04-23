n = int(input())

i = 0
while n > 0:
    if i == 0:
        n -= 1
    else:
        n -= 6 * i
    i += 1

print(i)