
n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)

def go():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i] == False:
            if len(s) >= 1 and i < s[-1]:
                continue
            visited[i] = True
            s.append(i)
            go()
            s.pop()
            visited[i] = False

go()