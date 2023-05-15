
n, s = map(int, input().split())

data = list(map(int, input().split()))

stack = []
result = 0
def go(depth):
    global result
    # print(stack)
    if stack and sum(stack) == s:
        result += 1
        # return
    for i in range(depth, n):
        stack.append(data[i])
        go(i + 1)
        stack.pop()

go(0)
print(result)