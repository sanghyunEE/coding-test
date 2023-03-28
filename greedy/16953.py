# import heapq

# a = int(input())

# h = []
# depth = 0
# insert = [3,1,5,6,7,8,2,4]

# for i in range(8):
#     heapq.heappush(h, insert[i])
# print(h)


a, b = map(int, input().split())

tree = [[a]]

depth = 0

while True:
    flag = 1 
    # 0 : 같은게 하나라도 있음 / -1 : 작은게 하나라도 있음 / +1 : B보다 다큼
    for i in tree[0]:
        if i == b:
            flag = 0
            break
        elif i < b:
            flag = -1
        else:
            continue
    if flag == 0:
        print(depth + 1)
        break
    elif flag == 1:
        print(-1)
        break
    else:
        temp = []
        for i in tree[0]:
            temp.append(i * 2)
            temp.append(int(str(i) + '1'))
        tree.append(temp)
        tree.pop(0)
        depth += 1

# https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-16953%EB%B2%88-A-B