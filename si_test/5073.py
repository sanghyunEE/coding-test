while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    # print(sorted([a, b, c])[0:2])
    if sorted([a, b, c])[-1] >= sum(sorted([a, b, c])[0:2]):
        print('Invalid')
        continue

    if a == b == c:
        print('Equilateral')
        continue
    elif (a == b) or (a == c) or (b == c):
        print('Isosceles')
        continue
    else:
        print('Scalene')
        continue
