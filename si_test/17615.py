n = int(input())

balls = list(input())

def remove_ball(color, arr):
    for _ in range(len(arr)):
        c = arr.pop()
        if c != color:
            arr.append(c)
            break
    return arr

def get_count(color, arr):
    # print(arr)
    temp = remove_ball(color, arr)
    # print(temp)
    return temp.count(color)

result = min(get_count('R', balls.copy()), get_count('R', balls.copy()[::-1]), get_count('B', balls.copy()), get_count('B', balls.copy()[::-1]))
print(result)
