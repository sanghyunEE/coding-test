from collections import Counter

s = input()
su = s.upper()

count = list(dict(Counter(su)).items())

count.sort(key = lambda x: x[1], reverse=True)

if len(count) >= 2 and count[0][1] == count[1][1]:
    print('?')
else:
    print(count[0][0])

# str -> 전체 소문자로 바꾸기, 전체 대문자로 바꾸기 내장 함수
# dict x[0] 또는 x[1] 기준으로 정렬하기