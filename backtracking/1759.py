
# 최소 한 개의 모음 (a e i o u)
# 최소 두 개의 자음

l, c = map(int, input().split())

data = list(input().split())
data.sort()

# print(data)


s = []
def go():
    if len(s) == l: # 유의 l로 해줘야지 4로 해버림
        m = 0
        j = 0
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1
        if m < 1 or j < 2:
            return
        print(''.join(s))
        return
    for c in data:
        if len(s) >= 1 and s[-1] > c:
            continue
        if c in s:
            continue
        s.append(c)
        go()
        s.pop()

go()