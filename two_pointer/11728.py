# list vs deque https://wellsw.tistory.com/122

from collections import deque

n, m = map(int, input().split())

qa = deque(list(map(int, input().split())))
qb = deque(list(map(int, input().split())))

result = deque()

while qa or qb:
    if not qa:
        result.extend(qb)
        break
    elif not qb:
        result.extend(qa)
        break
    if qa[0] < qb[0]:
        result.append(qa.popleft())
    else:
        result.append(qb.popleft())

print(' '.join(map(str, list(result))))