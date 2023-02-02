n = int(input())

words = []
for _ in range(n):
    words.append(input())

def asc(x):
    return len(x)

# softeer 기준 python 3.6 document 보고 str.lower 람다정규식 했음
# https://docs.python.org/ko/3.6/howto/sorting.html#sortinghowto
sorted_words = sorted(words, key = str.lower)
# alpha 기준으로 선 정렬 -> asc 순으로 하니까 되네..
sorted_words = sorted(sorted_words, key = asc)

for i in range(len(sorted_words)):
    if i != 0 and (sorted_words[i] == sorted_words[i-1]):
        continue
    print(sorted_words[i])

# sys.stdin.readline() 
# https://velog.io/@1204jh/1181
# https://wook-2124.tistory.com/468