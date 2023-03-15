from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)

result = []
while queue:
    i = 0
    for _ in range(k - 1):
        x = queue.popleft()
        queue.append(x)
    result.append(queue.popleft())

print('<' + str(result[0]), end = '')
for i in range(1, n):
    print(', ' + str(result[i]), end = '')
print('>')