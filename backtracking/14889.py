from itertools import combinations

n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]
member = list(range(n))
result = 100

for a in combinations(member, n // 2):
    b = list(set(member) - set(a))
    start, link = 0, 0
    for i in combinations(a, 2):
        start += s[i[0]][i[1]] + s[i[1]][i[0]]
    for i in combinations(b, 2):
        link += s[i[0]][i[1]] + s[i[1]][i[0]]
    result = min(result, abs(start - link))
print(result)
    

