import sys
input = sys.stdin.readline

temp = { 'all' : set(range(1, 21)), 'empty' : set() } 

S = set()

m = int(input())

for _ in range(m):
    CMD = input().split()
    if len(CMD) == 2:
        cmd, x = CMD[0], int(CMD[1])
    else:
        cmd = CMD[0]

    if cmd == 'add':
        if x in S:
            continue
        else:
            S.add(x)
    elif cmd == 'remove':
        if x not in S:
            continue
        else:
            S.remove(x)
    elif cmd == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cmd == 'all':
        S = temp['all']
    else:
        S = temp['empty']
    