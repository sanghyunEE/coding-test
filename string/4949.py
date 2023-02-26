from collections import deque

while True:
    flag = 0 # 0 yes / 1 no
    sentence = input().split('.')[0]
    if sentence == '': # 종료조건
        break
    if sentence == ' ':
        print('yes')
        continue

    stack = []
    for c in sentence:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' or c == ']':
            if len(stack) == 0:
                flag = 1
                break
            elif c == ')' and stack[-1] == '(':
                stack.pop(-1)
            elif c == ']' and stack[-1] == '[':
                stack.pop(-1)
            else:
                flag = 1
                break
        else:
            continue
    if flag == 1:
        print('no')    
    else:
        print('yes')


