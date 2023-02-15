n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)

prev = 0
for i in range(n):
    w = data[i] * (i + 1)
    if prev > w:
        continue # break가 되면 안돼! 
    else:
        prev = w

print(prev)

# 반례
# 5
# 27 23 15 11 11