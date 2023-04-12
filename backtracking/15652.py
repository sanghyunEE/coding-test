
n, m = map(int, input().split())

s = []
def go():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if len(s) >= 1 and s[-1] > i:
            continue
        s.append(i)
        go()
        s.pop()

go()