import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())
data.sort()

s, e = 0, n - 1
result = 0
while s != e:
    temp = data[s] + data[e]
    if temp == x:
        result += 1
        s += 1
    elif temp > x:
        e -= 1
    else:
        s += 1

print(result)