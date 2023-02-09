'''
# 내가 푼거 
n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
result = [0] * m

from collections import Counter
card = dict(Counter(card))

for i in find:
    if i not in card.keys():
        print(0, end=' ')
    else:
        print(card[i], end=' ') # 마지막 공백도 허용해주는 듯
'''
# 다양한 풀이 : https://chancoding.tistory.com/45