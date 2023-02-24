from collections import deque

while True:
    sentence = input().split('.')[0]
    if sentence == '': # 종료조건
        break
    if sentence == ' ':
        print('yes')
        break
    stack = []
    queue = deque()
    for c in sentence:
        temp = []
        if c == '(' or c == '[':
            stack.append(c)
            temp.append(c)
        elif c == ')' or c == ']':
            queue.append(c)
            temp.append(c)
    # print(stack, queue)
    if temp[0] == ')' or temp[0] == ']':
        print('no')
        break
    if len(stack) != len(queue):
        print('no')
        break
    else:
        
