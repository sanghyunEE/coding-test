has_generator = [False] * 10036

for i in range(1, 10001):
    result = i
    for j in str(i):
        result += int(j)
    has_generator[result] = True

for i in range(1, 10001):
    if has_generator[i] == False:
        print(i)
