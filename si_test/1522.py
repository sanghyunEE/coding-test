
s = input()

b_cnt = 0
for c in s:
    if c == 'b': b_cnt += 1

result = 1001
for i in range(len(s)):
    if i + b_cnt > len(s):
        temp = s[i:len(s)] + s[:b_cnt - (len(s) - i)]
    else:
        temp = s[i:b_cnt + i]
    # print(temp)
    count = 0
    for c in temp:
        if c == 'a': count += 1
    result = min(result, count)

print(result)