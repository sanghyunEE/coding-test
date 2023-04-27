# s -> t를 만들 수 있는지 체킹하면 발산적임
# 따라서, t 에서 소거를 해가며 s를 만들 수 있는 지는 수렴적임

s = list(input())
t = list(input())

stack = list(t)
result = 0
def go():
    global result
    if len(stack) == len(s):
        if stack == s:
            # print(stack, '같아')
            result = 1
        else:
            pass
            # print(stack, '달라')
        return
    if stack[0] == 'B':
        stack.reverse()
        stack.pop()
        go()
        stack.append('B')
        stack.reverse()

    if stack[-1] == 'A':
        stack.pop()
        go()
        stack.append('A')
go()
print(result)