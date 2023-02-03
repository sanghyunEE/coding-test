n, m = map(int, input().split())

data = [x for x in range(1, n + 1)]

from itertools import permutations

result = list(permutations(data, m))

for i in result:
    for j in i:
        print(j, end=' ')
    print()


# documetation 보고 풀었음\

# 근데 백트래킹으로 풀어야지 ㅇㅇ 순열 문제는