n = int(input())
n_array = sorted(list(map(int, input().split())))

m = int(input())
m_array = list(map(int, input().split()))

from bisect import bisect_right, bisect_left

def is_in(x):
    count = bisect_left(n_array, x) - bisect_right(n_array, x)
    if count == 0:
        return 0
    else:
        return 1

for i in m_array:
    print(is_in(i))

# set 으로 줄이고 -> if ___ in ___ 구문 활용하면 o(1) 이라는데?
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python
# https://otugi.tistory.com/256