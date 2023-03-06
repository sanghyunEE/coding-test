import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()

    temp = 0
    result = 0
    for c in s:
        if c == 'O':
            temp += 1
            result += temp
        else:
            temp = 0
            continue
    print(result)