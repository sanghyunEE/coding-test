n, m = map(int, input().split())

listen = []
look = []

for _ in range(n):
    listen.append(input())
for _ in range(m):
    look.append(input())

# counter의 시간복잡도는 o(n)임
from collections import Counter

array = listen + look

count = dict(Counter(array))
count = list(count.items())

result = list(filter(lambda x: x[1] >= 2 , count))
result.sort(key= lambda x: x[0]) # heapify 가능한가? 문자열대상으로?
print(len(result))
for i in result:
    print(i[0])

# https://wook-2124.tistory.com/476
# 내가 푼것도 맞다.