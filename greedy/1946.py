
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    data = []
    for _ in range(n):
        x, y = map(int, input().split())
        data.append((x, y))
    data.sort() # nlog(n)

    result = 0
    prev_y = 0
    for t in data:
        x, y = t
        if x == 1:
            result += 1
            prev_y = y
            continue
        else:
            if y < prev_y:
                result += 1
                prev_y = y
    print(result)


    

