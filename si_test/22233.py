import sys
input = sys.stdin.readline


n, m = map(int, input().split())

keyword = set()
for _ in range(n):
    keyword.add(input().rstrip())

blog = []
for _ in range(m):
    kw = input().rstrip().split(',')
    blog.append(set(kw))

# print(keyword)
# print(len(keyword))
# print(blog)

for k in blog: # 200,000
    # keyword = keyword - k
    for i in k:
        if i in keyword:
            keyword.discard(i)
    print(len(keyword))
    
# set 관련 자료
# https://velog.io/@juntree/Python-ListDictSet%EC%9D%98-%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-Big-O
# https://dev.plusblog.co.kr/41