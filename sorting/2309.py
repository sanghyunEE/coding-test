from itertools import combinations

data = []
for _ in range(9):
    data.append(int(input()))

array = list(combinations(data, 7))

result = []
for i in array:
    if sum(i) == 100:
        result = result + list(i)
        result.sort()
        break
for i in result:
    print(i)

# 세가지 방법론
# https://ji-gwang.tistory.com/244