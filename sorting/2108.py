import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

minus = [0] * 4001
zero = 0
plus = [0] * 4001

for i in data:
    if i < 0:
        minus[abs(i)] += 1
    elif i == 0:
        zero += 1
    else:
        plus[i] += 1

sorted_data = []
for i in range(1, 4001):
    for _ in range(minus[i]):
        sorted_data.append(-i)
sorted_data.reverse()

for _ in range(zero):
    sorted_data.append(0)

for i in range(1, 4001):
    for _ in range(plus[i]):
        sorted_data.append(i)

# print(sorted_data)

# 계수정렬  범위 : -4000 ~ 4000 이상 이하의 정수 

# 산술 평균
print(round(sum(data) / n))

# 중앙 값
print(sorted_data[n // 2])

# 최빈 값
current = 0 # 개수
result = []
for i in range(1, 4001):
    if current == minus[i]:
        result.append(-i)
    elif current < minus[i]:
        result = []
        result.append(-i)
        current = minus[i]
result.reverse()

# print(current, '@')
if current == zero:
        result.append(0)
elif current < zero:
    result = []
    result.append(0)
    current = zero

# print(current, '@@')
# print()
for i in range(1, 4001):
    if current == plus[i]:
        result.append(i)
    elif current < plus[i]:
        result = []
        result.append(i)
        current = plus[i]

# print(result)
if len(result) >= 2:
    print(result[1])
else:
    print(result[0])

# 범위
print(max(data) - min(data))