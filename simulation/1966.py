from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    queue = deque(data)
    zip_queue = deque()
    for i, j in zip(data, range(n)):
        zip_queue.append((i, j))

    result = 0
    while True:
        array = list(queue)
        if len(array) == 1:
            result += 1
            break
        if queue[0] < max(array[1:len(array)]):
            t = queue.popleft()
            queue.append(t)
            t = zip_queue.popleft()
            zip_queue.append(t)
        else:
            queue.popleft()
            t = zip_queue.popleft()
            result += 1
            if t[1] == m:
                break

    print(result)
