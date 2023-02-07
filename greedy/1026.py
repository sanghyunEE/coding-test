n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b, reverse=True)
temp = [-1] * n
copy_b = b.copy()

for x, y in zip(sorted_a, sorted_b):
    idx = copy_b.index(y)
    temp[idx] = x
    copy_b[idx] = -1

print(sum([x * y for x, y in zip(temp, b)]))

# 답은 맞는데 틀림이라고 나옴
# 깊은 복사로 b 카피했음

# https://yoonsang-it.tistory.com/44
# list.pop(idx) 이용해서 푸는 거 적응 하자 !!!!