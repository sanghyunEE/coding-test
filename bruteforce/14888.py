from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
exp_count = list(map(int, input().split()))

exp = ['+', '-', '*', '/']
temp = []
for i, j in zip(exp, exp_count):
    for _ in range(j):
        temp.append(i)


permut = list(permutations(temp, n - 1))

maximum = -int(1e9)
minimum = int(1e9)


for p in permut:
    result = data[0]
    for e, i in zip(p, data[1:]):
        if e == '+':
            result += i
        elif e == '-':
            result -= i
        elif e == '*':
            result *= i
        else:
            result = result // i + 1
    if maximum < result:
        print(p)
    maximum = max(maximum, result)
    minimum = min(minimum, result)

print(maximum)
print(minimum)



